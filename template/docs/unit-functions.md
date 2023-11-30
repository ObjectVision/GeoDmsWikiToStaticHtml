---
title: unit-functions
layout: default
parent: operator
nav_order: 47
---
Unit [operators-and-functions](operators-and-functions) are used to define and get information of [unit](unit), like [range](range) and [lowerbound](lowerbound)

-   [baseunit](baseunit) - *configure values units as base units, e.g. meter or second.*

<!-- -->

-   [tiledunit](tiledunit) - *configure segmented/tiled domain unit*

<!-- -->

-   [nrofrows](nrofrows) - *set the number of elements of a domain unit*
-   [range](range) - *sets the range for a unit*
-   [cat_range](cat_range) - *sets the range for a categorical unit*
-   [gridset](gridset) - *configures a grid domain with a projection to a coordinate system*

<!-- -->

-   [lowerbound](lowerbound) - *the minimum allowed value for the unit argument*
-   [upperbound](upperbound) - *the maximum allowed value for the unit argument*
-   [boundcenter](boundcenter) - *the mean value for the unit argument*
-   [boundrange](boundrange) - *the size of the range of the unit*

<!-- -->

-   [domainunit](domainunit) - *a reference to the domain unit of attribute a*
-   [valuesunit](valuesunit) - *a reference to the values unit of attribute a*
-   [defaultunit](defaultunit) - *the literal valuetype*

<!-- -->

-   [getprojectionbase](getprojectionbase) - *get the unit used for the coordinate system*
-   [getprojectionoffset](getprojectionoffset) - *get the coordinate of the top left grid cell in the coordinate system*
-   [getprojectionfactor](getprojectionfactor) - *get the gridsize in both X and Y directions.*
-   [getmetricfactor](getmetricfactor) - *get the factor in the metric of the unit used for the coordinate system*