// Global imports
#include <iostream>
#include <cstdlib>
#include <cstring>

// Local imports
#include "graph.hpp"
#include "../graphimage/graphviz.hpp"

// Graph

void Graph::init_matrix(int graphsize){

    this->distance_matrix = (int **)calloc(graphsize, sizeof(int *));
    
    for (size_t i = 0; i < graphsize; i++)
    {
        this->distance_matrix[i] = (int *)calloc(graphsize, sizeof(int));
    }

}

void Graph::set_distance(int x, int y, int distance){
    this->distance_matrix[x][y] = distance;
}

int Graph::get_distance(int x, int y){
    return this->distance_matrix[x][y];
}

Node *Graph::add_node(Node node) {

    if (node.get_id() != -1) {
        for (size_t i = 0; i < this->nodes.size(); i++) {
            if (this->nodes[i].get_id() == node.get_id()) {
                return &(this->nodes[i]);
            }
        }
    }
    if (node.get_id() == -1)
    {
        node.set_id(this->nodes.size());
    }
    this->nodes.push_back(node);
    return &(this->nodes[this->nodes.size() - 1]);
}

Node Graph::get_node(size_t index) {
    return this->nodes[index];
}

std::vector<Node> Graph::get_nodes(){
    return this->nodes;
}


// Util
