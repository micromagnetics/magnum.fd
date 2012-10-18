#ifndef DEMAG_STATIC_H
#define DEMAG_STATIC_H

#include "config.h"
#include "matrix/matty.h"

enum {
        INFINITE_NONE=0,
        INFINITE_POS_X=(1<<0),
        INFINITE_NEG_X=(1<<1),
        INFINITE_POS_Y=(1<<2),
        INFINITE_NEG_Y=(1<<3),
        INFINITE_POS_Z=(1<<4),
        INFINITE_NEG_Z=(1<<5),
};

VectorMatrix CalculateStrayfieldForCuboid(
	// mesh size
	int dim_x, int dim_y, int dim_z,
	double delta_x, double delta_y, double delta_z,
	// select magnetization: 1 A/m in x, y, or z direction (0, 1, or 2).
	int cuboid_mag_dir,
	// cuboid position, size and optionally infinite extent
	Vector3d cuboid_pos, // position of cuboid edge at local (0,0,0)
	Vector3d cuboid_size, // cuboid size in x,y,z dirs
	// A combination of INFINITE_xyz flags.
	// For infinite dimensions, the corresponding cuboid_size component must be zero.
	// Not all combinations of infinite dimensions are allowed.
	int cuboid_infinity 
);

#endif
