// Global imports
#include <cmath>
#include <iostream>
#include <utility>

// Local imports
#include "graph.hpp"

// Graph

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

void Graph::print_coords() {
    for (size_t i = 0; i < this->nodes.size(); i++) {
        this->nodes[i].print_coord();
    }
}

void Graph::generate_edges() {
    size_t n_neighbors;
    double distance;
    std::pair<int, double> furthest;
    coord current_node, possible_neighbor;
    n_neighbors = floor(log2(this->nodes.size()));
    std::vector<node_distance> neighbors;
    for (size_t i = 0; i < this->nodes.size(); i++) {
        neighbors.clear();
        current_node = this->nodes[i].get_coord();
        // Find n closest neighbors
        for (size_t j = 0; j < this->nodes.size(); j++) {
            if (i != j) {  // avoid calculate in the same coord
                possible_neighbor = this->nodes[j].get_coord();
                // Calc the distance between coordinates
                distance = distance_coords(&current_node, &possible_neighbor);
                if (neighbors.size() < n_neighbors) {  // Not enough neighbors evaluated
                    // Add neighbor
                    neighbors.push_back({&(this->nodes[j]), distance});
                } else {
                    // Get furthest point with a pair <{index}, {distance}>
                    furthest = get_furthest(neighbors);
                    if (furthest.second > distance) {  // Found a coord that is closer than one in the neighbors
                        neighbors[furthest.first].distance = distance;
                        neighbors[furthest.first].node = &(this->nodes[j]);
                    }
                }
            }
        }
        // With the n closest neighbors, create edges
        for (size_t j = 0; j < neighbors.size(); j++) {
            this->add_edge(&(this->nodes[i]), neighbors[j].node, neighbors[j].distance, true);
        }
    }
}

void Graph::add_edge(Node *origin, Node *destiny, double value, bool add_equals) {
    Edge edge{origin, destiny, value};
    this->add_edge(edge, add_equals);
}

void Graph::print_edges() {
    for (Edge edge : this->edges) {
        edge.print_aresta();
    }
}

void Graph::add_edge(Edge edge, bool add_equals) {
    // TODO: Check if origin and destiny in nodes
    bool origin, destiny;
    origin = false;
    destiny = false;
    if (!add_equals)
    {
        for (size_t i = 0; i < this->edges.size(); i++)
        {
            if (edge.get_origin()->get_id() == this->edges[i].get_origin()->get_id() && edge.get_destiny()->get_id() == this->edges[i].get_destiny()->get_id())
            {
                return;
            }
            if (edge.get_origin()->get_id() == this->edges[i].get_destiny()->get_id() && edge.get_destiny()->get_id() == this->edges[i].get_origin()->get_id())
            {
                return;
            }
        }
    }
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

long int Graph::get_node_index(Node *node) {
    for (size_t i = 0; i < this->nodes.size(); i++) {
        if (this->nodes[i].get_id() == node->get_id()) {
            return i;
        }
    }
    return -1;
}

Node *Graph::get_node(size_t index) {
    return &this->nodes[index];
}

long int Graph::get_node_index(long int id) {
    if (id == -1) return -1;
    for (size_t i = 0; i < this->nodes.size(); i++) {
        if (this->nodes[i].get_id() == id) {
            return i;
        }
    }
    return -1;
}

void Graph::clear() {
    this->edges.clear();
    this->nodes.clear();
}

short int Graph::is_brothers(Node *child_one, Node *child_two) {
    size_t i, j;
    bool is_father_of_one;
    for (i = 0; i < this->nodes.size(); i++) {
        // TODO: Remove childs from origin
        is_father_of_one = false;
        for (j = 0; j < this->edges.size(); j++) {
            if (this->edges[j].get_origin()->get_id() == this->nodes[i].get_id() && this->edges[j].get_color() == PURPLE) {
                if (this->edges[j].get_destiny()->get_id() == child_one->get_id() || this->edges[j].get_destiny()->get_id() == child_two->get_id()) {
                    if (is_father_of_one) {
                        return true;
                    }
                    is_father_of_one = true;
                }
            }
        }
    }
    return false;
}

void Graph::bfs(Graph *bfs_graph) {
    bfs_graph->clear();
    size_t t, i, j;
    size_t current_node, neighbor;
    long int bfs_neighbor_index;
    t = 0;
    std::vector<size_t> vector_de_entrada(this->nodes.size());
    std::vector<size_t> aux_queue;

    // Set root for search
    // i walks the nodes
    // j walks the edges
    for (i = 0; i < this->nodes.size(); i++) {
        if (vector_de_entrada[i] == 0) {
            this->nodes[i].set_level(0);
            t += 1;
            vector_de_entrada[i] = t;
            aux_queue.push_back(i);
            while (!aux_queue.empty()) {
                current_node = aux_queue.front();
                // Add node to bfs_graph
                Node *bfs_current_node;
                bfs_current_node = bfs_graph->add_node(this->nodes[current_node]);
                aux_queue.erase(aux_queue.begin());

                for (j = 0; j < this->edges.size(); j++) {
                    if (this->edges[j].get_origin()->get_id() == this->nodes[current_node].get_id()) {
                        neighbor = this->edges[j].get_destiny()->get_id();
                    } else if (this->edges[j].get_destiny()->get_id() == this->nodes[current_node].get_id()) {
                        neighbor = this->edges[j].get_origin()->get_id();
                    } else {  // Não é vizinho
                        continue;
                    }
                    Node *bfs_neighbor;
                    if (vector_de_entrada[neighbor] == 0) {
                        // First time in this node, add to bfs graph
                        bfs_neighbor = bfs_graph->add_node(this->nodes[neighbor]);
                        bfs_neighbor->set_level(bfs_current_node->get_level() + 1);
                        t += 1;
                        vector_de_entrada[neighbor] = t;
                        Edge bfs_edge{bfs_current_node, bfs_neighbor, this->edges[j].get_value()};
                        bfs_edge.set_color(COLORS::PURPLE);
                        bfs_graph->add_edge(bfs_edge, false);
                        aux_queue.push_back(neighbor);
                    } else {
                        // Will never be -1, I hope
                        bfs_neighbor_index = bfs_graph->get_node_index(neighbor);
                        bfs_neighbor = bfs_graph->get_node(bfs_neighbor_index);
                        Edge bfs_edge{bfs_current_node, bfs_neighbor, this->edges[j].get_value()};
                        if (bfs_neighbor->get_level() == bfs_current_node->get_level()) {
                            // Verify parenty
                            if (bfs_graph->is_brothers(bfs_current_node, bfs_neighbor)) {  // Brothers
                                bfs_edge.set_color(COLORS::BLACK);
                            } else {  // Cousins
                                bfs_edge.set_color(COLORS::YELLOW);
                            }
                        } else if (bfs_neighbor->get_level() == bfs_current_node->get_level() + 1) {  // Uncle Bob
                            bfs_edge.set_color(COLORS::GREEN);
                        }
                        if (bfs_edge.get_color() != COLORS::WHITE) {
                            bfs_graph->add_edge(bfs_edge, false);
                        }
                    }
                }
            }
        }
    }
}

std::pair<int, double> Graph::get_furthest(std::vector<node_distance> neighbors) {
    std::pair<int, double> furthest;
    furthest.first = 0;
    furthest.second = neighbors[0].distance;
    for (size_t i = 1; i < neighbors.size(); i++) {
        if (furthest.second < neighbors[i].distance) {
            furthest.first = i;
            furthest.second = neighbors[i].distance;
        }
    }
    return furthest;
}

// Util
