#ifndef _graph_h
#define _graph_h

#include <stddef.h>

typedef struct Nodo Nodo;
typedef struct Lista Lista;
typedef struct Graph Graph;


struct Nodo{
    int vertice;
    Nodo *proximo;
};

struct Lista{
    Nodo *head;
};

struct Graph{
    int num_vertices;
    Lista **lista_vertices;
};

size_t TAM_MATRIZ;

void count_matrix_size();
void init_matriz(size_t ***);
void print_matriz(size_t **);
void get_matriz(size_t ***);
void make_graph(Graph *, size_t **);
void print_graph(Graph *);
void add_nodo(Lista *, int );
void alloc_vertices(Graph *);



#endif
