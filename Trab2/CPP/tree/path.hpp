#pragma once

// Global headers imports
#include "vector"
// Local headers imports
#include "../graph/node.hpp"
#include "../graph/graph.hpp"
// Typedefs
// Structs & Classes

class Path {
   public:
    Path(int, std::vector<Node>, Graph);
    void get_shortest_path(std::vector<Node>, std::vector<Node>, Node, Node, int);
    std::vector<Node> get_path();
    int get_distance();

   private:
    std::vector<Node> path;
    int distance;
    Graph graph;
};

// Headers
