// Global imports
#include <iostream>
// Local imports
#include "edge.hpp"

// Edge
Edge::Edge(Node* origin, Node* destiny, double value) : origin{origin}, destiny{destiny}, value{value} {
}

void Edge::print_aresta(){
    std::cout << "Origin: " << origin->get_id() << "\tDestiny: " << destiny->get_id() << "\tValue: " << value << std::endl;
}
