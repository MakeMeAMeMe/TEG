// Global imports
#include <iostream>
#include <string>

// Local imports
#include "graph/graph.hpp"
#include "graphimage/graphviz.hpp"
#include "methods/min.hpp"
#include "methods/ord_pesos.hpp"
#include "methods/path.hpp"

// Defines
#define GRAPHSIZE 10
#define CITIES \
    { "Joinville", "Itajai", "Florianopolis", "Blumenau", "Sao Jose", "Chapeco", "Jaragua do Sul", "Criciuma", "Brusque", "Balneario Camboriu" }
#define DISTANCE_CITIES                                                                                                                                    \
    {                                                                                                                                                      \
        {0, 89, 177, 98, 173, 513, 50, 357, 115, 98}, {89, 0, 96, 53, 92, 585, 98, 276, 34, 12}, {177, 96, 0, 140, 10, 550, 188, 195, 100, 81},            \
            {98, 53, 140, 0, 139, 478, 65, 337, 41, 73}, {173, 92, 10, 139, 0, 543, 180, 194, 95, 75}, {513, 585, 550, 478, 543, 0, 487, 531, 517, 540},   \
            {50, 98, 188, 65, 180, 487, 0, 370, 101, 106}, {357, 276, 195, 337, 194, 531, 370, 0, 285, 265}, {115, 34, 100, 41, 95, 517, 101, 285, 0, 42}, \
        { 98, 12, 81, 73, 75, 540, 106, 265, 42, 0 }                                                                                                       \
    }

int main() {
    int distance_cities[GRAPHSIZE][GRAPHSIZE] = DISTANCE_CITIES;
    std::string cities[GRAPHSIZE] = CITIES;

    // making initial graph
    Graph graph;
    graph.init_matrix(GRAPHSIZE);

    // add matrix to the graph matrix
    for (size_t i = 0; i < GRAPHSIZE; i++) {
        for (long int j = 0; j < GRAPHSIZE; j++) {
            // add nodes if its the first time here
            if (i == 0) {
                Node aux = Node{j, cities[j]};
                graph.add_node(aux);
            }
            graph.set_distance(i, j, distance_cities[i][j]);
        }
    }
    // Ordenacao de pesos
    for (size_t i = 0; i < GRAPHSIZE; i++) {
        OrdemPesos ordem{graph};
        // pick the shortest_path of each initial node
        ordem.get_shortest_path(graph.get_node(i));
        ordem.print_path();
    }

    // Minimos sucessivos

    Min min{0, {}, graph};
    for (size_t i = 0; i < GRAPHSIZE; i++) {
        // pick the shortest_path of each initial node
        min.get_shortest_path(graph.get_nodes(), {}, graph.get_node(i), graph.get_node(i), 0);
    }

    min.print_path();

    // Construcao de arvores

    Path path{0, {}, graph};
    for (size_t i = 0; i < GRAPHSIZE; i++) {
        // pick the shortest_path of each initial node
        path.get_shortest_path(graph.get_nodes(), {}, graph.get_node(i), graph.get_node(i), 0);
    }

    path.print_path();

    return 0;
}
