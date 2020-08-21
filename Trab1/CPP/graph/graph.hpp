#pragma once

// Global headers imports
#include <cstdlib>
#include <utility>
#include <vector>

// Local headers imports
#include "../color/color.hpp"
#include "../graphimage/graphviz.hpp"
#include "edge.hpp"
#include "node.hpp"

// Defines

// Typedefs
typedef struct node_distance node_distance;

// Structs & Classes

struct node_distance {
    Node *node;
    double distance;
};

class Graph {
   public:
    Node *add_node(Node);
    void print_coords();
    void print_edges(Graphviz, bool);
    void generate_edges();
    void add_edge(Node *, Node *, double, bool);
    void add_edge(Edge, bool);
    long int get_node_index(Node *);
    long int get_node_index(long int);
    short int is_brothers(Node*, Node*);
    Node *get_node(size_t);
    void dfs(Graph *);
    void bfs(Graph *);
    std::pair<int, double> get_furthest(std::vector<node_distance>);
    void clear();

   private:
    std::vector<Node> nodes;
    std::vector<Edge> edges;
    void _dfs(Node *, size_t *, std::vector<size_t> *, std::vector<size_t> *, Graph *);
};

// Headers
