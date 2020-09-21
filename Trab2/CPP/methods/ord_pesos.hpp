// Global headers imports
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
// Local headers imports
#include "../graph/graph.hpp"
#include "../graph/node.hpp"

struct Grau {
    size_t grau_entrada;
    size_t grau_saida;
};

struct Edge {
    long origin;
    long destiny;
    int distance;
    bool operator<(const Edge& edge2) {
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
    bool have_cicle(std::vector<int>, long, std::vector<long>&, std::vector<long>&);

   public:
    OrdemPesos(Graph);
    void get_shortest_path(Node);
    void print_path();
};