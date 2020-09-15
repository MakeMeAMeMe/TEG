#pragma once

#include <cstdlib>
#include <string>
#include <fstream>

class Graphviz {
   public:
    Graphviz(std::string);
    void set_filename(std::string);
    std::string get_filename();
    void init_graph(int);
    void insert_edge();
    void end_graph();
    bool save_image();

   private:
    std::string filename;
};