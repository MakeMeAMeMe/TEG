// Global imports
#include <iostream>

// Local imports
#include "node.hpp"

// Node

Node::Node(coord* coordinate) : coordinate{*coordinate} {
    this->set_id(-1L);
}

void Node::set_id(long int id){
    this->id = id;
}

void Node::print_coord() {
    std::cout << "x: " << this->coordinate.x << "\ty:" << this->coordinate.y << std::endl;
}
