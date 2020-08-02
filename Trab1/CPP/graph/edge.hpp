#pragma once

// Global headers imports
#include <cstdlib>
// Local headers imports
#include "node.hpp"
// Typedefs
// Structs & Classes

class Edge {
   public:
    Edge(Node*, Node*, double);
    Node* get_origin() { return this->origin; };
    Node* get_destiny() { return this->destiny; };
    double get_value() { return this->value; };
    void set_color(size_t color) {this->color = color;};
    size_t get_color() {return this->color;};
    void print_aresta();

   private:
    Node* origin;
    Node* destiny;
    double value;
    size_t color;
};