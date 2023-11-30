---
title: grid-functions
layout: default
parent: operator
nav_order: 44
---
Grid [operators-and-functions](operators-and-functions) functions are used to calculate with [data-item](data-item) of [grid-domain](grid-domain), explicitly using the two-dimensional structure of data in [grid](grid), like [potential](potential) or [district](district).

-   [dist2](dist2) - *the distances in a grid towards a point data item*
-   [griddist](griddist) - *impedance in a grid towards the nearest point in a pointset, summing the resistances of the shortest path to the nearest point*

<!-- -->

-   [potential](potential) - *a neighborhood operation to sum the values of neighbouring cells in a grid, based on a kernel*
-   [proximity](proximity) - *a neighborhood operation to get the maximum value of neighbouring cells in a grid, based on a kernel*
-   [diversity](diversity) - *the number of different occurences in the neighbourhood of each cell in a grid*

<!-- -->

-   [district](district)   - *adjacent (horizontal & vertical, not diagonal) grid cell values with the same values*
-   [district_8](district_8) - *adjacent (horizontal & vertical & diagonal) grid cell values with the same values*

<!-- -->

-   [raster_merge](raster_merge) - *to merge data from smaller to larger grids, e.g. to combine country grids to a European grid*