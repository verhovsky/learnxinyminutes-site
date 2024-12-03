#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <stdlib.h>

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

int main() {
    Py_Initialize();

    char* code = "def hello_world():\n    print('Hello, world!')";
    char* highlighted_html = highlight_code(code, "python");
    if (highlighted_html) {
        printf("%s\n", highlighted_html);
        free(highlighted_html);
    }

    Py_Finalize();
    return 0;
}