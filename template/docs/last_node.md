---
title: last_node
layout: default
nav_exclude: true
---
*[network-functions](network-functions) last node*

## syntax

- last_node(*arc_polygon_dataitem*)

## definition

last_node(*arc_polygon_dataitem*) results in a [point](point) [data-item](data-item) with the coordinates of the **last point of an arc or polygon** of [argument](argument) *arc_polygon_dataitem*.

## description

Use the [arc2segm](arc2segm) function to split an [arc](arc) in [segment](segment).

## applies to

data item *arc_polygon_dataitem* with fpoint or dpoint [value-type](value-type) and [composition](composition) arc or polygon.

## example

<pre>
attribute&lt;fpoint&gt; last_node (Road) := <B>last_node(</B>road/geometry<B>)</B>;
</pre>

| road/geometry                                         |**last_node**         |
|-------------------------------------------------------|----------------------|
| {2 {399246, 112631}{398599, 111866}}                  | **{398599, 111866}** |
| {3 {398599, 111866}{399495, 111924} {401801, 111524}} | **{401801, 111524}** |
| {2 {401529, 114921}{398584, 114823}}                  | **{398584, 114823}** |

*domain Road, nr of rows = 3*

## see also

- [first_node](first_node)