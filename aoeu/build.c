#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <errno.h>
#include <ctype.h>
#include <stdbool.h>

#include <cmark.h>

void process_directory(const char *input_dir, const char *output_dir);
int is_markdown(const char *filename);

char* highlight_code(char* code, char* language) {
    PyObject *pygments, *lexers, *formatters, *lexer, *formatter, *highlight, *result;
    PyObject *first_args, *second_args, *kwargs;

    // Import Pygments modules
    pygments = PyImport_ImportModule("pygments");
    lexers = PyImport_ImportModule("pygments.lexers");
    formatters = PyImport_ImportModule("pygments.formatters");
    highlight = PyObject_GetAttrString(pygments, "highlight");

    // Create the lexer using get_lexer_by_name
    PyObject *get_lexer_by_name = PyObject_GetAttrString(lexers, "get_lexer_by_name");
    lexer = PyObject_CallFunction(get_lexer_by_name, "s", language);

    if (!lexer) {
        PyErr_Print();
        return NULL;
    }

    // Prepare formatter
    first_args = PyTuple_New(0);
    kwargs = PyDict_New();
    PyObject *formatter_obj = PyObject_GetAttrString(formatters, "HtmlFormatter");
    formatter = PyObject_Call(formatter_obj, first_args, kwargs);
    Py_DECREF(first_args);
    Py_DECREF(kwargs);

    if (!formatter) {
        PyErr_Print();
        return NULL;
    }

    // Prepare to call the highlight function
    second_args = PyTuple_Pack(3, PyUnicode_FromString(code), lexer, formatter);
    result = PyObject_CallObject(highlight, second_args);
    Py_DECREF(second_args);

    if (!result) {
        PyErr_Print();
        return NULL;
    }

    // Get the result string
    const char* highlighted_html = PyUnicode_AsUTF8(result);
    char* output = strdup(highlighted_html);
    Py_DECREF(result);

    return output;
}

#include <cmark.h>

void convert_md_to_html(const char *input_path, const char *output_path) {
    FILE *fp = fopen(input_path, "r");
    if (!fp) {
        perror("Error opening input file");
        return;
    }

    fseek(fp, 0, SEEK_END);
    long fsize = ftell(fp);
    fseek(fp, 0, SEEK_SET);

    char *contents = malloc(fsize + 1);
    fread(contents, 1, fsize, fp);
    fclose(fp);

    contents[fsize] = '\0';

    // Remove front matter if it exists
    char *markdown = contents;
    if (strncmp(contents, "---", 3) == 0) {
        char *end_fm = strstr(contents + 3, "\n---");
        if (end_fm) {
            markdown = end_fm + 4; // Skip the front matter end marker
            while (*markdown == '\n' || *markdown == '\r') markdown++; // Skip any extra newlines
        }
    }


    cmark_node *document = cmark_parse_document(markdown, strlen(markdown), CMARK_OPT_DEFAULT);
    free(contents);

    cmark_iter *iter = cmark_iter_new(document);
    cmark_event_type ev_type;
    cmark_node *node;

    while ((ev_type = cmark_iter_next(iter)) != CMARK_EVENT_DONE) {
        node = cmark_iter_get_node(iter);
        if (cmark_node_get_type(node) == CMARK_NODE_CODE_BLOCK) {
            const char *lang = cmark_node_get_fence_info(node);
            const char *code = cmark_node_get_literal(node);
            if (lang && strlen(lang) > 0) {
                char *highlighted = highlight_code((char *)code, (char *)lang);
                if (highlighted) {
                    cmark_node *new_node = cmark_node_new(CMARK_NODE_HTML_BLOCK);
                    cmark_node_set_literal(new_node, highlighted);
                    cmark_node_insert_after(node, new_node); // Insert new node after the code block
                    cmark_node_unlink(node); // Unlink the code block from the document
                    free(highlighted);
                }
            }
        }
    }

    char *html = cmark_render_html(document, CMARK_OPT_DEFAULT | CMARK_OPT_UNSAFE);
    cmark_iter_free(iter);
    cmark_node_free(document);

    FILE *fout = fopen(output_path, "w");
    if (!fout) {
        perror("Error opening output file");
        free(html);
        return;
    }

    fprintf(fout, "%s", html);
    fclose(fout);
    free(html);
}

void process_directory(const char *input_dir, const char *output_dir) {
    DIR *dir = opendir(input_dir);
    if (!dir) {
        perror("Failed to open input directory");
        return;
    }

    if (mkdir(output_dir, 0777) == -1 && errno != EEXIST) {
        perror("Failed to create output directory");
        closedir(dir);
        return;
    }

    struct dirent *entry;
    while ((entry = readdir(dir)) != NULL) {
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0)
            continue;

        char full_input_path[1024];
        snprintf(full_input_path, sizeof(full_input_path), "%s/%s", input_dir, entry->d_name);

        char full_output_path[1024];
        snprintf(full_output_path, sizeof(full_output_path), "%s/%s", output_dir, entry->d_name);

        struct stat statbuf;
        if (stat(full_input_path, &statbuf) == -1) {
            perror("Error getting file status");
            continue;
        }

        if (S_ISDIR(statbuf.st_mode)) {
            process_directory(full_input_path, full_output_path);
        } else if (is_markdown(entry->d_name)) {
            strcpy(strrchr(full_output_path, '.'), ".html");
            convert_md_to_html(full_input_path, full_output_path);
        }
    }

    closedir(dir);
}

int is_markdown(const char *filename) {
    const char *ext = strrchr(filename, '.');
    if (!ext) return 0;
    return strcasecmp(ext, ".md") == 0 || strcasecmp(ext, ".markdown") == 0;
}

int main(int argc, char **argv) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <input_dir> <output_dir>\n", argv[0]);
        return 1;
    }

    Py_Initialize();
    process_directory(argv[1], argv[2]);
    Py_Finalize();
    return 0;
}
