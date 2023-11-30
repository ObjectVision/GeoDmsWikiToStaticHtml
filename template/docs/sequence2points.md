---
title: sequence2points
layout: default
nav_exclude: true
---
*[geometric-functions](geometric-functions) sequence2points*

![](../assets/img/GUI/sequence2points_function.png)

## syntax

- sequence2points(*arc_polygon_data_item*)

## definition

sequence2points(*arc_polygon_data_item*) results in a new **[domain-unit](domain-unit) with all points** from the arcs/polygons of the *arc_polygon_data_item*

The function generates three [subitem](subitem):

1.  Point: a [data-item](data-item) with the points of all arcs/polygons of the *arc_polygon_data_item*
2.  SequenceNr: a [relation](relation) towards the domain unit of the *arc_polygon_data_item*
3.  Ordinal: a uint32 data item  with the order of each point in the *arc_polygon_data_item*

## applies to

data item *arc_polygon_data_item* with fpoint or dpoint [value-type](value-type) and composition type arc or polygon.

## example

<pre>
unit&lt;uint32&gt; RoadPointSet := <B>sequence2points(</B>road/geometry<B>)</B>;
</pre>

| road/geometry                                        |
|------------------------------------------------------|
| {2 {399246, 112631}{398599, 111866}}                 |
| {3 {398599, 111866}{399495, 111924} {401801,111524}} |
| {2 {401529, 114921}{398584, 114823}}                 |

*domain Road, nr of rows = 3*

| **point**            | **SequenceNr** | **Ordinal** |
|----------------------|---------------:|------------:|
| **{399246, 112631}** | **0**          | **0**       |
| **{398599, 111866}** | **0**          | **1**       |
| **{398599, 111866}** | **1**          | **0**       |
| **{399495, 111924}** | **1**          | **1**       |
| **{401801, 111524}** | **1**          | **2**       |
| **{401529, 114921}** | **2**          | **0**       |
| **{398584, 114823}** | **2**          | **1**       |

*domain RoadPointSet, nr of rows = 7*

## see also

- [points2sequence](points2sequence)
- [arc2segm](arc2segm)