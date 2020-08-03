#pragma once

// Global headers imports
#include <vector>
#include <utility>
#include <cstdlib>

// Local headers imports
#include "edge.hpp"
#include "node.hpp"

// Defines
#define BLUE 1
#define RED 2

// Typedefs
typedef struct node_distance node_distance;

// Structs & Classes

struct node_distance {
    Node *node;
    double distance;
};

class Graph {
   public:
    void add_node(Node);
    void print_coords();
    void print_edges();
    void generate_edges();
    void add_edge(Node*, Node*, double);
    void add_edge(Edge);
    int get_node_index(Node*);
    void dfs(Graph*);
    void bfs(Graph*);
    std::pair <int, double> get_furthest(std::vector<node_distance>);

   private:
    std::vector<Node> nodes;
    std::vector<Edge> edges;
    void _dfs(Node*, size_t*, std::vector<size_t>*, std::vector<size_t>*, Graph*);
};

// Headers