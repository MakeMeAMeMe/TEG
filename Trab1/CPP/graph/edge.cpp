// Global imports
#include <iostream>
// Local imports
#include "edge.hpp"

// Edge
Edge::Edge(Node* origin, Node* destiny, double value) : origin{origin}, destiny{destiny}, value{value} {
    this->set_color(COLORS::WHITE);
}

void Edge::print_aresta(bool printconn) {
    std::cout << "Origin: " << origin->get_id() << "\tDestiny: " << destiny->get_id() << "\tValue: " << value;
    if (printconn)
    {
        std::cout << "\tCor: " << this->get_color_name();
    }
    
    std::cout << std::endl;
}

Node* Edge::get_origin() {
    return this->origin;
}
Node* Edge::get_destiny() {
    return this->destiny;
}
double Edge::get_value() {
    return this->value;
}
void Edge::set_color(COLORS color) {
    this->color = color;
}
COLORS Edge::get_color() {
    return this->color;
}
void Edge::set_color_name(std::string color_name){
    this->color_name = color_name;
}
std::string Edge::get_color_name(){
    return this->color_name;
}
