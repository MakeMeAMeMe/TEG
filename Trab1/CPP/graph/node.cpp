// Global imports
#include <iostream>

// Local imports
#include "node.hpp"

// Node

Node::Node(coord* coordinate) : coordinate{*coordinate} {
    this->set_index(0L);
}

void Node::set_index(size_t index){
    this->index = index;
}

void Node::print_coord() {
    std::cout << "x: " << this->coordinate.x << "\ty:" << this->coordinate.y << std::endl;
}
