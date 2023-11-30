---
title: vector-to-grid-processing-example
layout: default
nav_exclude: true
---
*[configuration-examples](configuration-examples) Vector to Grid processing*

This script explores different options for making [grid](grid) versions of [vector-data](vector-data). The following examples are part of this script

1. Configuring grids for different grid sizes.
2. Configuring a grid at a small sizes and aggregate this to a larger cells is included. This can be used to make a grid based on maximum area (see also <https://www.geodms.nl/mantis/view.php?id=58>)
3. Configuring an [arc](arc) data source, making a grid version of these arcs and combine these with a landuse grid.

## download

- [configuration/data](https://www.geodms.nl/downloads/GeoDMS_Academy/geodms_academy_vector_2_grid_20210120.zip)

## concepts

- [grid/raster analysis](https://geogra.uah.es/patxi/gisweb/GISModule/GIST_Raster.htm)

## functions

- [poly2grid](poly2grid)
- [modus](modus)
- [arc2segm](arc2segm)
- [dyna_point](dyna_point)
- [invert](invert)