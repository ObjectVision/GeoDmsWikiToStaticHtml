---
title: vector-data
layout: default
nav_exclude: true
---
Vector data is data with a one-dimensional [domain-unit](domain-unit), with at least one [feature-attribute](feature-attribute) and optionally other [attribute](attribute) for the same domain unit.

![](../assets/img/GUI/vectordomain.png)

**The feature attribute refers to the coordinates of the vectors.** 

The GeoDMS supports the following vector types:
- [point](point): point data, the feature attribute refers to one coordinate per entry.
- [arc](arc): arc data, the feature attribute refers to at least two coordinates per entry.
- [polygon](polygon): polygon data, the feature attribute refers to at least three coordinates per entry.

It is important to know the [coordinate-system](coordinate-system) of your vector data, as they may effect the results of functions like [arc_length](arc_length) and [connect_info](connect_info).

## vector sources

Vector data in GeoDMS applications is read from (and can also be written to some of) the following formats:
- [esri-shapefile](esri-shapefile) (point, arc, polygon)
- [geopackage](geopackage) (point, arc, polygon)
- [ascii-files](ascii-files) : [csv](csv) (point) and [xml](xml) (point, arc, polygon)
- [filegeodatabase](filegeodatabase) (point, arc, polygon)
- [postgis](postgis) (point, arc, polygon)
- [xml](xml)(point, arc, polygon)
- [fss](fss) files (point, arc, polygon)

## vector calculations

The GeoDMS contains multiple functions to calculate with the vector coordinates, see mainly the [geometric-functions](geometric-functions)  
