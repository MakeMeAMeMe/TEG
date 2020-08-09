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

coord Node::get_coord(){
    return this->coordinate;
}

long int Node::get_id(){
    return this->id;
}

void Node::set_level(long int level){
    this->level = level;
}
long int Node::get_level(){
    return this->level;
}
