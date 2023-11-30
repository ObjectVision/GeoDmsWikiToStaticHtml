---
title: grid-domain
layout: default
nav_exclude: true
---
![](../assets/img/GUI/grid_format.png)

A [grid](grid) domain is a two-dimensional [domain-unit](domain-unit), each cell is defined by a row and a column number.

This implies the [value-type](value-type) of the [domain-unit](domain-unit) is of type PointGroup.

Most grid domains in the GeoDMS are used to describe a part of the world, called [geographic-grid-domain](geographic-grid-domain).

Furthermore, grid domains are also in use to define [kernel](kernel) for [potential](potential) calcualtions. 

## grid functions

Most [operators-and-functions](operators-and-functions) in the GeoDMS work on [data-item](data-item) of one (table) of two (grid) dimensional domains.

There is group of functions that explicitly use the two-dimensional structure of grid domains, for instance to calculate nearby relations. 
This group is called [grid-functions](grid-functions).