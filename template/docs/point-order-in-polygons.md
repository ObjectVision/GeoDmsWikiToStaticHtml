---
title: point-order-in-polygons
layout: default
nav_exclude: true
---
For some [operators-and-functions](operators-and-functions) (like [union_polygon-(dissolve)](union_polygon-(dissolve))) the sequence order of points in a [polygon](polygon) matters.

## rules

The following rules apply to the sequence of points in a [polygon](polygon):

1.  outer rings need to be configured clock wise
2.  inner rings (lakes) are configured counter clock wise
3.  the first and the last point need to have the same coordinate

If the sequence of points is configured manually and used in the [sequence2points](sequence2points), always configure the correct sequence, although for the map and functions like [point_in_polygon](point_in_polygon) an incorrect sequence might not matter.

## validation

A way to test if the correct sequence is configured is by requesting the area of the [polygon](polygon) with the [area](area) function.
A positive value indicates a correct sequence, a negative value indicates the points are configured in the incorrect sequence