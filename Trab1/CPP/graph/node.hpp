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
    long int get_id() { return this->id; };
    void print_coord();
    void set_id(long int);

   private:
    coord coordinate;
    long int id;
};

// Headers
