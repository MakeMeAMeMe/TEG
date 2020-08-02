#pragma once

// Global headers imports
// Local headers imports
#include "../coordinate/coordinate.hpp"
// Typedefs
// Structs & Classes

class Node {
   public:
    Node(coord*);
    coord get_coord() { return this->coordinate; };
    size_t get_index() { return this->index; };
    void print_coord();
    void set_index(size_t);

   private:
    coord coordinate;
    size_t index;
};

// Headers
