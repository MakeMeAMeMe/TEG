// Global headers imports
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
// Local headers imports
#include "../graph/graph.hpp"
#include "../graph/node.hpp"

struct Grau {
    size_t grau_entrada;
    size_t grau_saida;
};

struct Edge {
    int origin;
    int destiny;
    int distance;
    bool operator<(const Edge& edge2){
        return this->distance < edge2.distance;
    }
};

typedef Grau Grau; 
typedef Edge Edge; 

class OrdemPesos {
   private:
    int distance;
    std::vector<Node> path;
    Graph graph;
    std::vector<Edge> edges;
    std::map<int, Grau> graus; 
    bool sort_edge(Edge, Edge);

   public:
    OrdemPesos(Graph);
    void get_shortest_path(std::vector<Node>, std::vector<Node>, Node, Node, int);
    void print_path();
};