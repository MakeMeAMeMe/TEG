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
    void set_color(COLORS);
    COLORS get_color();
    void print_aresta(bool);
    void set_color_name(std::string);
    std::string get_color_name();

   private:
    Node* origin;
    Node* destiny;
    double value;
    COLORS color;
    std::string color_name;
};