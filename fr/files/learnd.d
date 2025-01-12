// Commençons par un classique
module hello;

import std.stdio;

// args n'est pas obligatoire
void main(string[] args) {
    writeln("Bonjour le monde !");
}
import std.stdio;

void main() {
    //Les conditions et les boucles sont classiques.
    for(int i = 0; i < 10000; i++) {
        writeln(i);
    }

    // On peut utiliser auto pour inférer automatiquement le
    // type d'une variable.
    auto n = 1;

    // On peut faciliter la lecture des valeurs numériques
    // en y insérant des `_`.
    while(n < 10_000) {
        n += n;
    }

    do {
        n -= (n / 2);
    } while(n > 0);

    // For et while sont très utiles, mais en D, on préfère foreach.
    // Les deux points : '..', créent un intervalle continu de valeurs
    // incluant la première mais excluant la dernière.
    foreach(i; 1..1_000_000) {
        if(n % 2 == 0)
            writeln(i);
    }

    // On peut également utiliser foreach_reverse pour itérer à l'envers.
    foreach_reverse(i; 1..int.max) {
        if(n % 2 == 1) {
            writeln(i);
        } else {
            writeln("Non !");
        }
    }
}
// Ici, 'T' est un paramètre de type. Il est similaire au <T> de C++/C#/Java.
struct LinkedList(T) {
    T data = null;

    // Utilisez '!' pour instancier un type paramétré.
    // Encore une fois semblable à '<T>'
    LinkedList!(T)* next;
}

class BinTree(T) {
    T data = null;

    // S'il n'y a qu'un seul paramètre de template,
    // on peut s'abstenir de mettre des parenthèses.
    BinTree!T left;
    BinTree!T right;
}

enum Day {
    Sunday,
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
}

// Utilisez alias pour créer des abreviations pour les types.
alias IntList = LinkedList!int;
alias NumTree = BinTree!double;

// On peut tout aussi bien créer des templates de function !
T max(T)(T a, T b) {
    if(a < b)
        return b;

    return a;
}

// On peut utiliser le mot-clé ref pour s'assurer que quelque chose est passé
// par référence, et ceci, même si a et b sont d'ordinaire passés par valeur.
// Ici ils seront toujours passés par référence à 'swap()'.
void swap(T)(ref T a, ref T b) {
    auto temp = a;

    a = b;
    b = temp;
}

// Avec les templates, on peut également passer des valeurs en paramètres.
class Matrix(uint m, uint n, T = int) {
    T[m] rows;
    T[n] columns;
}

auto mat = new Matrix!(3, 3); // T est 'int' par défaut
// Considérons une classe paramétrée avec les types 'T' et 'U'
class MyClass(T, U) {
    T _data;
    U _other;
}

// Et des méthodes "getter" et "setter" comme suit:
class MyClass(T, U) {
    T _data;
    U _other;

    // Les constructeurs s'appellent toujours 'this'.
    this(T t, U u) {
        // Ceci va appeller les setters ci-dessous.
        data = t;
        other = u;
    }

    // getters
    @property T data() {
        return _data;
    }

    @property U other() {
        return _other;
    }

    // setters
    @property void data(T t) {
        _data = t;
    }

    @property void other(U u) {
        _other = u;
    }
}

// Et on l'utilise de cette façon:
void main() {
    auto mc = new MyClass!(int, string)(7, "seven");

    // Importer le module 'stdio' de la bibliothèque standard permet
    // d'écrire dans la console (les imports peuvent être locaux à une portée)
    import std.stdio;

    // On appelle les getters pour obtenir les valeurs.
    writefln("Earlier: data = %d, str = %s", mc.data, mc.other);

    // On appelle les setter pour assigner de nouvelles valeurs.
    mc.data = 8;
    mc.other = "eight";

    // On appelle les setter pour obtenir les nouvelles valeurs.
    writefln("Later: data = %d, str = %s", mc.data, mc.other);
}
import std.algorithm : map, filter, reduce;
import std.range : iota; // construit un intervalle excluant la dernière valeur.

void main() {
    // On veut un algorithme qui affiche la somme de la liste des carrés
    // des entiers paires de 1 à 100. Un jeu d'enfant !

    // On se contente de passer des expressions lambda en paramètre à des templates.
    // On peut fournir au template n'importe quelle fonction, mais dans notre
    // cas, les lambdas sont pratiques.
    auto num = iota(1, 101).filter!(x => x % 2 == 0)
                           .map!(y => y ^^ 2)
                           .reduce!((a, b) => a + b);

    writeln(num);
}
import std.stdio;
import std.parallelism : parallel;
import std.math : sqrt;

void main() {
    // On veut calculer la racine carrée de tous les nombres
    // dans notre tableau, et profiter de tous les coeurs
    // à notre disposition.
    auto arr = new double[1_000_000];

    // On utilise un index et une référence à chaque élément du tableau.
    // On appelle juste la fonction parallel sur notre tableau !
    foreach(i, ref elem; parallel(arr)) {
        ref = sqrt(i + 1.0);
    }
}
