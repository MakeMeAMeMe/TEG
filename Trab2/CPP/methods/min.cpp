// Global imports
#include <iostream>

// Local imports
#include "min.hpp"

// Node

Min::Min(int distance, std::vector<Node> path, Graph graph) : distance{distance}, path{path}, graph{graph} {
}

void Min::get_shortest_path(std::vector<Node> nodes, std::vector<Node> path, Node initial_node, Node actual_node, int distance){
    
    path.push_back(actual_node);

    for (size_t i = 0; i < nodes.size(); i++)
    {
        if (nodes[i].get_id() == actual_node.get_id())
        {
            nodes.erase(nodes.begin() + i);
            break;
        }
    }
    
    if (nodes.size() == 0)
    {
        distance += this->graph.get_distance(actual_node.get_id(), initial_node.get_id());
        path.push_back(initial_node);
        if ((distance < this->distance) || this->distance == 0)
        {
            this->distance = distance;
            this->path = path;
        }
        return;
    }

    int smaller_distance=2000, smaller_node;

    // find the smaller distance
    for (size_t i = 0; i < nodes.size(); i++)
    {
        int node_distance = graph.get_distance(actual_node.get_id(), nodes[i].get_id());
        if (node_distance < smaller_distance)
        {
            smaller_distance = node_distance;
            smaller_node = i;
        }
        
    }

    get_shortest_path(nodes, path, initial_node, nodes[smaller_node], distance + this->graph.get_distance(actual_node.get_id(), nodes[smaller_node].get_id()));
}

void Min::print_path(){
    std::cout<<"\nMenor distancia (Minimos sucessivos): "<<distance<<"m\n\n";

    std::cout<<"Caminho encontrado:\n\n";

    for (size_t i = 0; i < path.size(); i++)
    {
        std::cout<<path[i].get_nome()<<", ";
    }
    std::cout<<std::endl;
}

