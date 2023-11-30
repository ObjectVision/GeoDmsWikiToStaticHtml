---
title: point_isnearby
layout: default
nav_exclude: true
---
*[geometric-functions](geometric-functions) point_is_NearBy*

## syntax
- point_isNearby(a, b, margin)

## definition
point_isNearby(a, b, margin) results in a boolean [data item](https://github.com/ObjectVision/GeoDMS/wiki/data_item) indicating if the values of [point](point) [data-item](data-item) a <B>are within the margin</B> *margin* of the corresponding values of data item b.

## description

With floating point data values, due to round offs, it can be useful to compare results and accept a margin in which the comparison still results in a True value. Use the point_isNearby function in stead of the [eq](eq) function for point data in these cases.

The comparison between two missing values results in the value True.

The point_isNearBy function can be used in the similar manner as the [float_isnearby](float_isnearby) function.

## applies to

Data items *a*, *b*, *margin* with fpoint/dpoint value type

## conditions

1. [domain-unit](domain-unit) of the [argument](argument) must match or be [void](void) ([literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)%7Cliterals) or [parameter](parameter) can be compared to data items of any domain).
2. [argument](argument) must have matching:
   - [value-type](value-type)

## see also
- [float_isnearby](float_isnearby)