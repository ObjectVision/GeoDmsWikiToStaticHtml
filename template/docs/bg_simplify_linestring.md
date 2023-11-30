---
title: bg_simplify_linestring
layout: default
nav_exclude: true
---
*[geometric-functions](geometric-functions) bg_simplify_linestring*

![](../assets/img/GUI/bg_simplify_linestring.png)

## syntax

- bg_simplify_linestring(*arc_data_item*, *simplifyfactor*)

## description

bg_simplify_linestring(*arc_data_item, simplifyfactor*) results in a data item with the geometry of the <B>*arc_data_item*, in which the geometric structure is simplified</B>. Near points are combined to a single point. What is near is configured with the *simplifyfactor*, a [parameter](parameter) indicating for which distance points are combined. No metric needs to be configured for the *simplifyfactor,* it is using the [metric](metric) of the [coordinate-system](coordinate-system).

The *bg_* prefix of the function name indicates that the implementation of operator uses [boost geometry](https://www.boost.org/doc/libs/1_80_0/libs/geometry/doc/html/index.html)
library, more specifically, the [simplify](https://www.boost.org/doc/libs/1_80_0/libs/geometry/doc/html/geometry/reference/algorithms/simplify/simplify_3.html) function.

## applies to

- [attribute](attribute) *arc_data_item* with an point [value-type](value-type)
- [parameter](parameter) *simplifyfactor* with a [float64](float64) value type

## conditions

1. The [composition](composition) type of the *arc_data_item* item needs to be arc.
2. The order of points in the *arc_data_item* needs to be clockwise for exterior bounds and counter clockwise for holes in polygons (right-hand-rule).

## since version

8.031

## example
<pre>
attribute&lt;fpoint&gt; geometry_simplified (polygon, district) := <B>bg_simplify_linestring(</B>road/geometry, 10.0<B>)</B>;
</pre>

## see also:
- [bg_simplify_polygon](bg_simplify_polygon)
- [bg_simplify_multi_polygon](bg_simplify_multi_polygon)