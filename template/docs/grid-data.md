---
title: grid-data
layout: default
nav_exclude: true
---
![](../assets/img/GUI/grid_format.png)

Grid data are numeric or boolean [attribute](attribute) for a [grid-domain](grid-domain). 

In GeoDMS applications, grid data is often spatial, meaning it describes a rectangle of the earth surface.

The spatial reference of grid data is derived from the [projection](projection) information of the domain unit.

## read/write
Grid data in GeoDMS projects can be read from and or written to the following formats:
- [geotiff](geotiff) format (advised format)
- BMP (undocumented)
- [ascii-grid](ascii-grid)
- [arc-info-binary-grid](arc-info-binary-grid)

## calculations
Most functions in the GeoDMS apply to attributes of both one-dimensional as well as grid domains. 

The [grid-functions](grid-functions) apply only to attributes of grid domains, as they calculate with the two-dimensional structure of the data.

## see also
- [vector-data](vector-data)

