#pragma once

// Global headers imports
#include "vector"
// Local headers imports
#include "../graph/node.hpp"
#include "../graph/graph.hpp"
// Typedefs
// Structs & Classes

class Min {
   public:
    Min(int, std::vector<Node>, Graph);
    void get_shortest_path(std::vector<Node>, std::vector<Node>, Node, Node, int);
    void print_path();

   private:
    int distance;
    std::vector<Node> path;
    Graph graph;
};

// Headers
