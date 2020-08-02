// Global imports
#include <iostream>
// Local imports
#include "edge.hpp"

// Edge
Edge::Edge(Node* origin, Node* destiny, double value) : origin{origin}, destiny{destiny}, value{value} {
}

void Edge::print_aresta(){
    std::cout << "Origin: " << origin->get_index() << "\tDestiny: " << destiny->get_index() << "\tValue: " << value << std::endl;
}
