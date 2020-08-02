#pragma once

// Global headers imports
// Local headers imports

// Typedefs
typedef struct coord coord;
// Structs & Classes

struct coord {
    float x;
    float y;
};

double distance_coords(coord*, coord*);
