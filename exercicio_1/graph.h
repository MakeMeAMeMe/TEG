#ifndef _graph_h
#define _graph_h

#include <stddef.h>

#define MATRIX_SIZE 20
#define FILE_PATH "./grafo.txt"

size_t get_line_degree(size_t**, int);
bool ensure_regular_graph(size_t**);
bool ensure_simple_graph(size_t**);
bool ensure_connected_graph(size_t**);
bool check_visits(bool*);
void iterate_graph(size_t**, bool * *, int);
void fill_visits(bool * *);
void get_matrix(size_t * **);
void print_graph(size_t**);
void initialize_graph(size_t *** );

#endif