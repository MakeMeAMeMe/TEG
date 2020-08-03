// Global imports
#include <cmath>
#include <iostream>

// Local imports
#include "graph.hpp"

// Graph

void Graph::add_node(Node node) {
    if (node.get_id() != -1) {
        for (size_t i = 0; i < this->nodes.size(); i++) {
            if (this->nodes[i].get_id() == node.get_id()) {
                return;
            }
        }
    }
    node.set_id(this->nodes.size());
    this->nodes.push_back(node);
}

void Graph::print_coords() {
    for (size_t i = 0; i < this->nodes.size(); i++) {
        this->nodes[i].print_coord();
    }
}

void Graph::generate_edges() {
    size_t n_neighbors;
    double distance, biggest_distance;
    coord current_node, possible_neighbor;
    n_neighbors = floor(log2(this->nodes.size()));
    std::vector<node_distance> neighbors;
    for (size_t i = 0; i < this->nodes.size(); i++) {
        neighbors.clear();
        current_node = this->nodes[i].get_coord();
        biggest_distance = 0;
        // Find n closest neighbors
        for (size_t j = 0; j < this->nodes.size(); j++) {
            if (i != j) {  // avoid calculate in the same coord
                possible_neighbor = this->nodes[j].get_coord();
                // Calc the distance between coordinates
                distance = distance_coords(&current_node, &possible_neighbor);
                if (neighbors.size() < n_neighbors) {  // Not enough neighbors evaluated
                    // Add neighbor
                    neighbors.push_back({&(this->nodes[j]), distance});
                    // Upd biggest distance
                    if (biggest_distance < distance) {
                        biggest_distance = distance;
                    }
                } else if (biggest_distance > distance) {  // Found a coord that is closer than one in the neighbors
                    // Find coord that have the biggest distance
                    for (size_t k = 0; k < neighbors.size(); k++) {
                        if (neighbors[k].distance == biggest_distance) {
                            // Upd this position to have the new coord
                            neighbors[k].distance = distance;
                            neighbors[k].node = &(this->nodes[j]);
                            break;
                        }
                    }
                    // Upd biggest distance
                    biggest_distance = distance;
                }
            }
        }
        // With the n closest neighbors, create edges
        for (size_t j = 0; j < neighbors.size(); j++) {
            this->add_edge(&(this->nodes[i]), neighbors[j].node, neighbors[j].distance);
        }
    }
}

void Graph::add_edge(Node* origin, Node* destiny, double value) {
    Edge edge{origin, destiny, value};
    this->add_edge(edge);
}

void Graph::print_edges() {
    for (Edge edge : this->edges) {
        edge.print_aresta();
    }
}

void Graph::add_edge(Edge edge) {
    // TODO: Check if origin and destiny in nodes
    bool origin, destiny;
    origin = false;
    destiny = false;
    for (size_t i = 0; i < this->nodes.size(); i++) {
        if (this->nodes[i].get_id() == edge.get_origin()->get_id()) {
            origin = true;
        } else if (this->nodes[i].get_id() == edge.get_destiny()->get_id()) {
            destiny = true;
        }
        if (origin && destiny) {
            this->edges.push_back(edge);
            break;
        }
    }
}

int Graph::get_node_index(Node* node) {
    for (size_t i = 0; i < this->nodes.size(); i++) {
        if (this->nodes[i].get_id() == node->get_id()) {
            return i;
        }
    }
    return -1;
}

void Graph::dfs(Graph* dfs_graph) {
    size_t t;
    t = 0;
    std::vector<size_t> input_depth(this->nodes.size());
    std::vector<size_t> output_depth(this->nodes.size());
    // Set root for search
    size_t root_index;
    root_index = std::rand() % this->nodes.size();
    Node* root;
    root = &(this->nodes[root_index]);
    // Exec search
    _dfs(root, &t, &input_depth, &output_depth, dfs_graph);
}

void Graph::_dfs(Node* node, size_t* t, std::vector<size_t>* input_depth, std::vector<size_t>* output_depth, Graph* dfs_graph) {
    *t += 1;
    size_t node_index, neighbor_index;
    node_index = node->get_id();
    (*input_depth)[node_index] = *t;
    coord origin, destiny;
    Node* neighbor = nullptr;
    // TODO: Add Node to graph, prob add id to node for later comparisson
    Node dfs_node{*node};
    dfs_graph->add_node(dfs_node);
    for (size_t i = 0; i < this->edges.size(); i++) {
        if (this->edges[i].get_origin()->get_id() == node->get_id()) {
            neighbor = this->edges[i].get_destiny();
        } else if (this->edges[i].get_destiny()->get_id() == node->get_id()) {
            neighbor = this->edges[i].get_origin();
        } else {  // Não é vizinho
            continue;
        }
        Node dfs_neighbor{*neighbor};
        dfs_graph->add_node(dfs_neighbor);
        neighbor_index = neighbor->get_id();
        if ((*input_depth)[neighbor_index] == 0) {
            std::cout << "BLUE Edge" << std::endl;
            Edge edge{&dfs_node, &dfs_neighbor, distance_coords(&origin, &destiny)};
            edge.set_color(BLUE);
            dfs_graph->add_edge(edge);

            _dfs(neighbor, t, input_depth, output_depth, dfs_graph);
        } else {
            bool is_father;
            is_father = false;
            for (size_t j = 0; j < dfs_graph->edges.size(); j++) {
                if (dfs_graph->edges[j].get_origin()->get_id() == dfs_neighbor.get_id() && dfs_graph->edges[j].get_destiny()->get_id() == dfs_neighbor.get_id()) {
                    is_father = true;
                    break;
                }
            }
            if ((*output_depth)[neighbor_index] == 0 && !is_father) {
                // Add a red edge from neighbor to node
                std::cout << "RED Edge" << std::endl;
                origin = node->get_coord();
                destiny = neighbor->get_coord();
                Edge edge{&dfs_neighbor, &dfs_node, distance_coords(&origin, &destiny)};
                edge.set_color(RED);
                dfs_graph->add_edge(edge);
            }
        }
    }
    *t += 1;
    (*output_depth)[node_index] = *t;
}

void Graph::bfs(Graph* dfs_graph) {
    size_t t;
    t = 0;
    std::vector<size_t> aux_q(this->nodes.size());
    
    // Set root for search
    size_t root_index;
    root_index = std::rand() % this->nodes.size();
    Node* root;
    root = &(this->nodes[root_index]);
}

// Util

void loaded() {
    std::cout << "Graph loaded" << std::endl;
}
