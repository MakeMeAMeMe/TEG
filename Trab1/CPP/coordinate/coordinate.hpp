#pragma once

// Global headers imports
// Local headers imports

// Typedefs
typedef struct coord coord;
// Structs & Classes

struct coord {
    double x;
    double y;
};

double distance_coords(coord*, coord*);
