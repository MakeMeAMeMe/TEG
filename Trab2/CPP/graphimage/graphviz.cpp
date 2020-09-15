#include <cstdlib>
#include <fstream>
#include <graphviz/gvc.h>

#include "graphviz.hpp"

Graphviz::Graphviz(std::string filename) : filename{filename}{}

std::string Graphviz::get_filename()
{
    return this->filename;
}

void Graphviz::set_filename(std::string filename)
{
    this->filename = filename;
}

void Graphviz::init_graph(int graph)
{
    std::ofstream file;
    file.open(filename + ".dot");
    file << "digraph G" << graph << " {" << std::endl;
    file.close();
}

// void Graphviz::insert_edge(Edge *edge)
// {
//     std::ofstream file;
//     file.open(filename + ".dot", std::ios::app);
//     file << "\"" << edge->get_origin()->get_id() << "\" -> \"" 
//     << edge->get_destiny()->get_id() << "\" [ color=\"" << edge->get_color_name() << "\", dir=none ]" << std::endl;
//     file.close();
// }

void Graphviz::end_graph()
{
    std::ofstream file;
    file.open(filename + ".dot", std::ios::app);
    file << "}" << std::endl;
    file.close();
}

bool Graphviz::save_image()
{
  GVC_t *gvc;
  Agraph_t *g;
  FILE *fp;
  gvc = gvContext();
  fp = fopen((filename + ".dot").c_str(), "r");
  g = agread(fp, 0);
  gvLayout(gvc, g, "dot");
  gvRender(gvc, g, "png", fopen((filename + ".png").c_str(), "w"));
  gvFreeLayout(gvc, g);
  agclose(g);
  return (gvFreeContext(gvc));
}
