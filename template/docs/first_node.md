---
title: first_node
layout: default
nav_exclude: true
---
*[network-functions](network-functions) first node*

## syntax

- first_node(*arc_polygon_dataitem*)

## definition

first_node(*arc_polygon_dataitem*) results in a [point](point) [data-item](data-item) with the coordinates of the **first point of an arc or polygon** of [argument](argument) *arc_polygon_dataitem*.

## description

Use the [arc2segm](arc2segm) function to split an [arc](arc) in [segment](segment).

## applies to

data item *arc_polygon_dataitem* with fpoint or dpoint [value-type](value-type) and [composition](composition) type arc or polygon.

## example

<pre>
attribute&lt;fpoint&gt; first_node (Road) := <B>first_node(</B>road/geometry<B>)</B>;
</pre>

| road/geometry                                        |**first_node**        |
|------------------------------------------------------|----------------------|
| {2 {399246, 112631}{398599, 111866}}                 | **{399246, 112631}** |
| {3 {398599, 111866}{399495, 111924} {401801,111524}} | **{398599, 111866}** |
| {2 {401529, 114921}{398584, 114823}}                 | **{401529, 114921}** |

*domain Road, nr of rows = 3*

## see also

- [last_node](last_node)