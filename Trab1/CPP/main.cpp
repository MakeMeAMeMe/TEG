// Global imports
#include <ctime>
#include <iostream>
#include <random>
#include <cstdlib>

// Local imports
#include "graph/graph.hpp"

// Defines
// constexpr unsigned short int N_GRAPHS = 4;
constexpr unsigned short int N_GRAPHS = 1;
//constexpr unsigned int GRAPHS[] = {50, 100, 200, 300};
constexpr unsigned int GRAPHS[] = {5};

int main() {
    // Seed Rand
    std::srand(std::time(nullptr));
    // Generate points
    for (size_t i = 0; i < N_GRAPHS; i++) {
        // Construct Graph
        Graph graph, dfs_graph;
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
        graph.print_edges();
        // Run dfs
        graph.dfs(&dfs_graph);
        // Print Results
    }

    return 0;
}
