#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "graph.h"

int main(void) {
    Graph *grafo = malloc(sizeof(Graph *));
    size_t **matriz;
    count_matrix_size();
    init_matriz(&matriz);
    get_matriz(&matriz);
    print_matriz(matriz);
    make_graph(grafo, matriz);
    print_graph(grafo);
    return 0;
}

void count_matrix_size() {
    int count = 0;
    FILE *file = fopen("grafo.txt", "r");
    char *p = malloc(1 * sizeof(char *));
    while(1){
        fscanf(file, "%c", p);
        if(*p == '\n'){
            break;
        }else if(*p == ' '){
            continue;
        }else{
            count++;
        }
    }
    TAM_MATRIZ = count;
    fclose(file);
}

void init_matriz(size_t ***matriz) {
    (*matriz) = calloc(TAM_MATRIZ , sizeof(size_t *));

    for (size_t i = 0; i < TAM_MATRIZ ; i++)
    {
        (*matriz)[i] = calloc(TAM_MATRIZ , sizeof(size_t));
    }
}

void get_matriz(size_t ***matriz){
    FILE *file = fopen("grafo.txt", "r");
    char *p = malloc(1 * sizeof(char *));
    for (size_t i = 0; i < TAM_MATRIZ ; i++)
    {
        for (size_t j = 0; j < TAM_MATRIZ ; j++)
        {
            fscanf(file, "%c", p);
            if(*p == ' ' || *p == '\n'){
                j--;
                continue;
            }
            (*matriz)[i][j] = (size_t)*p - 48;
        }
    }

}

void print_matriz(size_t **matriz){

    for (size_t i = 0; i < TAM_MATRIZ ; i++)
    {
        for (size_t j = 0; j < TAM_MATRIZ ; j++)
        {
            printf("%lu ", matriz[i][j]);
        }

        printf("\n");
        
    }
    

}

void make_graph(Graph *grafo, size_t **matriz){
    alloc_vertices(grafo);

    for (size_t i = 0; i < TAM_MATRIZ; i++)
    {
        for (size_t j = 0; j < TAM_MATRIZ; j++)
        {
            if(matriz[i][j] == 1){
                add_nodo((grafo->lista_vertices)[i], j);
            }
        }
        
    }
}

void alloc_vertices(Graph *grafo){
    grafo->num_vertices = TAM_MATRIZ;
    grafo->lista_vertices = malloc(grafo->num_vertices * sizeof(Lista *));

    for (size_t i = 0; i < grafo->num_vertices; i++)
    {
        (grafo->lista_vertices)[i] = malloc(sizeof(Lista));
        (grafo->lista_vertices)[i]->head = NULL;
    }
    
}

void add_nodo(Lista *lista, int vertice){
    Nodo *nodo = malloc(sizeof(Nodo));
    nodo->proximo = NULL;
    nodo->vertice = vertice;
    if(lista->head == NULL){
        lista->head = nodo;

    }
    else{
        Nodo *aux;
        aux = lista->head;
        while (aux->proximo != NULL)
        {
            aux = aux->proximo;
        }
        aux->proximo = nodo;
        
    }
}   

void print_graph(Graph *grafo){
    Nodo *aux;

    for (size_t i = 0; i < grafo->num_vertices; i++)
    {
        aux = (grafo->lista_vertices)[i]->head;
        printf("\n| %lu |", i);
        for (size_t j = 0; aux != NULL ; j++)
        {
            printf(" -> | %d |", aux->vertice);
            aux = aux->proximo;
        }
        
    }
        printf("\n");
    
}