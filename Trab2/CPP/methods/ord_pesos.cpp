#include "./ord_pesos.hpp"

OrdemPesos::OrdemPesos(Graph graph) : graph{graph} {
    this->distance =0;
    this->path = std::vector<Node>();
    this->graus = std::map<int, Grau>();
    this->edges = std::vector<Edge>();
    for (size_t i = 0; i < this->graph.get_nodes().size(); i++) {
        this->graus[this->graph.get_node(i).get_id()] = {0, 0};
        for (size_t j = 0; j < this->graph.get_nodes().size(); j++) {
            if (i != j) {
                this->edges.push_back({(int)i, (int)j, this->graph.get_distance(i, j)});
            }
        }
    }
    std::sort(this->edges.begin(), this->edges.end());
}

void OrdemPesos::get_shortest_path(std::vector<Node> nodes, std::vector<Node> path, Node initial_node, Node actual_node, int distance) {
    int origin;
    int destiny;
    bool ciclo, completo;
    for (size_t i = 0; i < this->edges.size(); i++) {
        origin = this->edges[i].origin;
        destiny = this->edges[i].destiny;
        if (this->graus[origin].grau_entrada + this->graus[origin].grau_saida < 2 && this->graus[destiny].grau_entrada + this->graus[destiny].grau_saida < 2) {
            // Grau valido
            this->graus[origin].grau_entrada += 1;
            this->graus[destiny].grau_saida += 1;
            ciclo = true;
            completo = true;
            for (auto j = this->graus.begin(); j != this->graus.end(); j++) {
                if (j->second.grau_entrada + j->second.grau_saida == 0) {
                    completo = false;
                    break;
                }
                if (j->second.grau_entrada + j->second.grau_saida == 1) {
                    ciclo = false;
                    break;
                }
            }
            if (!completo && ciclo) {
                this->graus[origin].grau_entrada -= 1;
                this->graus[destiny].grau_saida -= 1;
            }
            // Checar ciclo
        }
    }
    // Montar path
    while(this->path.size() < this->graph.get_nodes().size()){

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
