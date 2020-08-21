// Global imports
#include <ctime>
#include <iostream>
#include <random>
#include <cstdlib>
#include <string>

// Local imports
#include "graph/graph.hpp"
#include "graphimage/graphviz.hpp"

// Defines
constexpr unsigned short int N_GRAPHS = 4;
// constexpr unsigned short int N_GRAPHS = 1;
constexpr unsigned int GRAPHS[] = {50, 100, 200, 300};
// constexpr unsigned int GRAPHS[] = {5};

int main() {
    // Seed Rand
    std::srand(std::time(nullptr));
    // Generate points
    for (size_t i = 0; i < N_GRAPHS; i++) {
        // Construct Graph
        Graph graph, dfs_graph, bfs_graph;
        std::string filename = "img_graph/G" + std::to_string(GRAPHS[i]);
        Graphviz graphviz(filename);
        graphviz.init_graph(GRAPHS[i]);
        for (size_t j = 0; j < GRAPHS[i]; j++) {
            // Generate GRAPHS[i] coordinates

            coord coordinate;

            coordinate.x = ((float)std::rand()) / RAND_MAX;
            coordinate.y = ((float)std::rand()) / RAND_MAX;

            Node node{&coordinate};

            graph.add_node(node);
        }
        graph.print_coords();
        graph.generate_edges();
        graph.print_edges(graphviz, true);
        graphviz.end_graph();
        if (GRAPHS[i] <= 100)
        {
            graphviz.save_image();
        }
        
        // Run bfs
        filename = ("img_tree/G" + std::to_string(GRAPHS[i]));
        graphviz.set_filename(filename);
        graphviz.init_graph(GRAPHS[i]);
        graph.bfs(&bfs_graph);
        // Print Results
        std::cout << "BFS GRAPH" << std::endl;
        bfs_graph.print_edges(graphviz, false);
        graphviz.end_graph();
        if (GRAPHS[i] <= 100)
        {
            graphviz.save_image();
        }
    }

    return 0;
}
