#pragma once

// Global headers imports
#include <cstdlib>
// Local headers imports
#include "node.hpp"
#include "../color/color.hpp"
// Typedefs
// Structs & Classes

class Edge {
   public:
    Edge(Node*, Node*, double);
    Node* get_origin();
    Node* get_destiny();
    double get_value();
    void set_color(COLORS color);
    COLORS get_color();
    void print_aresta();

   private:
    Node* origin;
    Node* destiny;
    double value;
    COLORS color;
};