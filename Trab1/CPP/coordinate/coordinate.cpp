#include "coordinate.hpp"
#include "cmath"

double distance_coords(coord* origin, coord* destiny){
    return sqrt((destiny->x - origin->x) * (destiny->x - origin->x) +
     (destiny->y - origin->y) * (destiny->y - origin->y));
}
