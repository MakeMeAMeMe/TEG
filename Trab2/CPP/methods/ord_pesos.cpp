#include "./ord_pesos.hpp"

OrdemPesos::OrdemPesos(Graph graph) : graph{graph} {
    this->distance = 0;
    this->path = std::vector<Node>();
    this->graus = std::map<int, Grau>();
    this->edges = std::vector<Edge>();
    for (size_t i = 0; i < this->graph.get_nodes().size(); i++) {
        this->graus[this->graph.get_node(i).get_id()] = {0, 0};
        for (size_t j = i + 1; j < this->graph.get_nodes().size(); j++) {
            this->edges.push_back({this->graph.get_node(i).get_id(), this->graph.get_node(j).get_id(), this->graph.get_distance(i, j)});
        }
    }
    std::sort(this->edges.begin(), this->edges.end());
    //for (size_t i = 0; i < this->edges.size(); i++) {
    //    std::cout << "Edge: " << this->edges[i].origin << " " << this->edges[i].destiny << " " << this->edges[i].distance << std::endl;
    //}
}

void OrdemPesos::get_shortest_path(Node initial_node) {
    int origin;
    int destiny;
    std::vector<int> used_edges = std::vector<int>();
    for (size_t i = 0; i < this->edges.size(); i++) {
        origin = this->edges[i].origin;
        destiny = this->edges[i].destiny;
        if (this->graus[origin].grau_entrada + this->graus[origin].grau_saida < 2 && this->graus[destiny].grau_entrada + this->graus[destiny].grau_saida < 2) {
            // Grau valido
            this->graus[origin].grau_entrada += 1;
            this->graus[destiny].grau_saida += 1;
            used_edges.push_back(i);
            std::vector<long> visited_nodes = std::vector<long>();
            std::vector<long> visited_edges = std::vector<long>();
            bool is_done = true;
            for (auto i = this->graus.begin(); i != this->graus.end(); i++) {
                if (i->second.grau_entrada + i->second.grau_saida != 2) {
                    is_done = false;
                    break;
                }
            }

            if (is_done) {
                this->distance += this->edges[i].distance;
                break;
            }
            if (!this->have_cicle(used_edges, this->edges[i].origin, visited_nodes, visited_edges)) {
                this->distance += this->edges[i].distance;
            } else {
                this->graus[origin].grau_entrada -= 1;
                this->graus[destiny].grau_saida -= 1;
                used_edges.pop_back();
            }
        }
    }
    //std::cout << "Graus" << std::endl;
    //for (auto i = this->graus.begin(); i != this->graus.end(); i++) {
    //    std::cout << "Node: " << i->first << " ";
    //    std::cout << i->second.grau_entrada + i->second.grau_saida;
    //    std::cout << std::endl;
    //}
    //
    //std::cout << "Used Edges" << std::endl;
    //for (size_t i = 0; i < used_edges.size(); i++) {
    //    std::cout << "Edge: " << this->edges[used_edges[i]].origin << " " << this->edges[used_edges[i]].destiny << std::endl;
    //}

    // Montar path
    Node actual_node{initial_node};
    this->path.push_back(actual_node);
    std::vector<int> node_visited = std::vector<int>();
    while (this->path.size() - 1 < this->graph.get_nodes().size()) {
        for (size_t i = 0; i < used_edges.size(); i++) {
            if (this->edges[used_edges[i]].origin == actual_node.get_id() && !(std::find(node_visited.begin(), node_visited.end(), this->edges[used_edges[i]].destiny) != node_visited.end())) {
                actual_node = this->graph.get_node_by_id(this->edges[used_edges[i]].destiny);
                node_visited.push_back(actual_node.get_id());

                path.push_back(actual_node);
                break;
            } else if (this->edges[used_edges[i]].destiny == actual_node.get_id() && !(std::find(node_visited.begin(), node_visited.end(), this->edges[used_edges[i]].origin) != node_visited.end())) {
                actual_node = this->graph.get_node_by_id(this->edges[used_edges[i]].origin);
                node_visited.push_back(actual_node.get_id());

                path.push_back(actual_node);
                break;
            }
        }
    }
}
void OrdemPesos::print_path() {
    std::cout << "\nMenor distancia (WIP): " << distance << "m\n";

    std::cout << "\nCaminho encontrado:\n\n";

    for (size_t i = 0; i < path.size(); i++) {
        std::cout << path[i].get_nome() << ", ";
    }
    std::cout << std::endl;
}
bool OrdemPesos::have_cicle(std::vector<int> used_edges, long id, std::vector<long>& visited_nodes, std::vector<long>& visited_edges) {
    visited_nodes.push_back(id);
    bool is_cicle = false;
    if (this->graus[id].grau_saida + this->graus[id].grau_entrada == 2) {
        for (size_t i = 0; i < used_edges.size(); i++) {
            if (!(std::find(visited_edges.begin(), visited_edges.end(), i) != visited_edges.end())) {
                if (this->edges[used_edges[i]].origin == id) {
                    visited_edges.push_back(i);
                    if (std::find(visited_nodes.begin(), visited_nodes.end(), this->edges[used_edges[i]].destiny) != visited_nodes.end()) {
                        return true;
                    }
                    is_cicle = this->have_cicle(used_edges, this->edges[used_edges[i]].destiny, visited_nodes, visited_edges);
                } else if (this->edges[used_edges[i]].destiny == id) {
                    visited_edges.push_back(i);
                    if (std::find(visited_nodes.begin(), visited_nodes.end(), this->edges[used_edges[i]].origin) != visited_nodes.end()) {
                        return true;
                    }
                    is_cicle = this->have_cicle(used_edges, this->edges[used_edges[i]].origin, visited_nodes, visited_edges);
                }
                if (is_cicle) {
                    return true;
                }
            }
        }
    }
    return false;
}
