#pragma once

// Global headers imports
// Local headers imports
#include "../coordinate/coordinate.hpp"
// Typedefs
// Structs & Classes

class Node {
   public:
    Node(coord*);
    coord get_coord();
    long int get_id();
    void print_coord();
    void set_id(long int);
    void set_level(long int);
    long int get_level();

   private:
    coord coordinate;
    long int level;
    long int id;
};

// Headers
