#pragma once

// Global headers imports
#include <vector>
// Local headers imports
// Typedefs
// Structs & Classes

class Node {
   public:
    Node(long int, std::string);
    long int get_id();
    void set_id(long int);
    std::string get_nome();

   private:
    long int id;
    std::string nome;
};

// Headers
