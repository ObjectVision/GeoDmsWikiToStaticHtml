---
title: poly2grid_untiled
layout: default
nav_exclude: true
---
*[geometric-functions](geometric-functions) poly2grid_untiled*

![](../assets/img/GUI/poly2grid_w400.png)

## syntax

- poly2grid_untiled(*polygon_data_item*, *gridunit*)

## definition

The poly2grid_untiled function results in **[grid](grid) [data-item](data-item) with a [relation](relation) to the [domain-unit](domain-unit)** of the *polygon_data_item*

The resulting data item has:

- as [domain-unit](domain-unit) the *gridunit* argument
- as [values-unit](values-unit) the [domain-unit](domain-unit) of the *polygon_data_item* [argument](argument)

## description

This function is the same as [poly2grid](poly2grid) but writes singly threaded on a single mutable shadow tile that is then split into separate tiles after rendering all polygons.
Compared to [poly2grid](poly2grid), this poly2grid_untiled function will:
- take longer to calculate (as it doesn't process tiles in parallel),
- use more memory (to store the intermediate mutable shadow tile), 
- but uses less CPU time (as polygons preparation is not repeated for each tile with which their bounding box intersects),
- the results are independent of the actual tiling (which could not be always true for [poly2grid](poly2grid) as the conversion to a tile-local coordinate system might cause tiling-dependent flip-cases).

## applies to

- data item *polygon_data_item* with a wpoint, spoint, upoint, ipoint, fpoint or dpoint [value-type](value-type)
- [unit](unit) *gridunit* with a wpoint, spoint upoint, ipoint, fpoint, dpoint value type

## conditions

1. The [composition](composition) type of the *polygon_data_item* needs to be polygon.
2. The [domain-unit](domain-unit) of the *polygon_data_item* must be of value type uint32.

## since version

8.7.0

## example

<pre>
attribute&lt;source/district&gt; DistrictGrid (gridunit/gridcel_10m) := 
   <B>poly2grid_untiled(</B>Source/District/border, gridunit/gridcel_10m<B>)</B>;
</pre>

## see also

- [poly2grid](poly2grid)
