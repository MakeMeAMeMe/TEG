// Global imports
#include <iostream>

// Local imports
#include "path.hpp"

// Node

Path::Path(int distance, std::vector<Node> path, Graph graph) : distance{distance}, path{path}, graph{graph} {
}

void Path::get_shortest_path(std::vector<Node> nodes, std::vector<Node> path, Node initial_node, Node actual_node, int distance){
    
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
            return;
        }
        
    }

    for (size_t i = 0; i < nodes.size(); i++)
    {
        // pick the shortest path of each node remaining
        get_shortest_path(nodes, path, initial_node, nodes[i], distance + this->graph.get_distance(actual_node.get_id(), nodes[i].get_id()));
    }
}

std::vector<Node> Path::get_path(){
    return this->path;
}

int Path::get_distance(){
    return this->distance;
}

