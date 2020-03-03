#include "graph.h"
#include <fstream>
#include <iostream>
using namespace std;

/**
 * TODO
 * 
 * Verificar graph regular
 *  - Verificar se a soma de todas as linhas é a mesma
 * Vericar graph simples
 *  - Diagonal principal nula e ponderamento == 1
 * Verificar graph desconexo
 * 
 * */

size_t get_line_degree(size_t **graph, int line) {
    size_t sum, j;
    sum = 0;
    for (j = 0; j < MATRIX_SIZE; j++) {
        sum += graph[line][j];
    }
    return sum;
}

bool ensure_regular_graph(size_t **graph) {
    size_t aux, degree, i;
    degree = get_line_degree(graph, 0);
    for (i = 1; i < MATRIX_SIZE; i++) {
        if (get_line_degree(graph, i) != degree) {
            return false;
        }
    }
    return true;
}

bool ensure_simple_graph(size_t **graph) {
    size_t i, j;
    for (i = 0; i < MATRIX_SIZE; i++) {
        for (j = 0; j < MATRIX_SIZE; j++) {
            if (i == j && graph[i][j] != 0) {
                return false;
            } else if (graph[i][j] != 0 && graph[i][j] != 1) {
                return false;
            }
        }
        cout << endl;
    }
    return true;
}

bool ensure_connected_graph(size_t **graph) {
    bool *visits = new bool[MATRIX_SIZE];
    fill_visits(&visits);
    iterate_graph(graph, &visits, 0);
    return check_visits(visits);
}

bool check_visits(bool *visits) {
    size_t i;
    for (i = 0; i < MATRIX_SIZE; i++) {
        if (visits[i] == 0) {
            return false;
        }
    }
    return true;
}

void iterate_graph(size_t **graph, bool **visits, int line) {
    size_t j;
    for (j = 0; j < MATRIX_SIZE; j++) {
        if (graph[line][j] > 0 && (*visits)[j] == false) {
            (*visits)[j] = true;
            iterate_graph(graph, visits, j);
        }
    }
}

void fill_visits(bool **visits) {
    size_t i;
    for (i = 0; i < MATRIX_SIZE; i++) {
        (*visits)[i] = false;
    }
}

void get_matrix(size_t ***graph) {
    ifstream arquivo;
    char aux;
    size_t i, j;
    arquivo.open(FILE_PATH, ios::in);
    for (i = 0; i < MATRIX_SIZE; i++) {
        for (j = 0; j < MATRIX_SIZE; j++) {
            arquivo >> aux;
            if (aux == '\n') {
                j--;
            } else {
                (*graph)[i][j] = ((size_t)aux) - 48;
            }
        }
    }
}

void print_graph(size_t **graph) {
    size_t i, j;
    for (i = 0; i < MATRIX_SIZE; i++) {
        for (j = 0; j < MATRIX_SIZE; j++) {
            cout << graph[i][j] << " ";
        }
        cout << endl;
    }
}

void initialize_graph(size_t ***graph) {
    size_t i, j;
    (*graph) = new size_t *[MATRIX_SIZE];
    for (i = 0; i < MATRIX_SIZE; i++) {
        (*graph)[i] = new size_t[MATRIX_SIZE];
        for (j = 0; j < MATRIX_SIZE; j++) {
            (*graph)[i][j] = 0;
        }
    }
}

int main(int argc, char const *argv[]) {
    size_t **graph;
    initialize_graph(&graph);
    get_matrix(&graph);
    print_graph(graph);
    if (ensure_regular_graph(graph)) {
        cout << "Grafo Regular" << endl;
    } else {
        cout << "Grafo não Regular" << endl;
    }
    if (ensure_simple_graph(graph)) {
        cout << "Grafo Simples" << endl;
    } else {
        cout << "Grafo não Simples" << endl;
    }
    if (ensure_connected_graph(graph)) {
        cout << "Grafo Conectado" << endl;
    } else {
        cout << "Grafo não Conectado" << endl;
    }
    return 0;
}
