// Global imports
#include <iostream>

// Local imports
#include "node.hpp"

// Node

Node::Node(long int id, std::string nome) : id{id}, nome{nome} {
    this->set_id(-1L);
}

void Node::set_id(long int id){
    this->id = id;
}

long int Node::get_id(){
    return this->id;
}

std::string Node::get_nome(){
    return this->nome;
}
