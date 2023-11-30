---
title: projection
layout: default
nav_exclude: true
---
Projection information is a set of parameters, defining the relation between a local grid and a [geographical coordinate system](https://en.wikipedia.org/wiki/Geographic_coordinate_system).

For multiple [grid-data](grid-data) the projection information is read from the grid files or accompanying [world files](https://en.wikipedia.org/wiki/World_file) (a GeoTiff file for example often has this information stored in a .tfw file in the same folder).

The projection information can also be explicitly configured in the GeoDMS configuration, see: [geographic-grid-domain](geographic-grid-domain).

The projection is presented in the [geodms-gui](geodms-gui) > Detail Pages > General > Projection for the geographic domain unit and all [attribute](attribute)  with this [domain-unit](domain-unit).

## contents

Projection information consists of the following set of parameters:

- pixel size in the x-direction in map units, often positive
- pixel size in the y-direction in map units, often negative
- x-coordinate of the center of the upper left pixel
- y-coordinate of the center of the upper left pixel

A world file can also contains rotation information, this is at the moment not (yet) used in the GeoDMS.