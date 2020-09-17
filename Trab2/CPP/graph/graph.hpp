#pragma once

// Global headers imports
#include <cstdlib>
#include <utility>
#include <vector>

// Local headers imports
#include "../graphimage/graphviz.hpp"
#include "node.hpp"

// Defines

// Typedefs
typedef struct node_distance node_distance;

// Structs & Classes

class Graph {
   public:
    Node *add_node(Node);
    Node get_node(size_t);
    std::vector<Node> get_nodes();
    void init_matrix(int);
    void set_distance(int, int, int);
    int get_distance(int, int);

   private:
    std::vector<Node> nodes;
    int **distance_matrix;
};

// Headers
