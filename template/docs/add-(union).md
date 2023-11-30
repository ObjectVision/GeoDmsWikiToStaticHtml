---
title: add-(union)
layout: default
nav_exclude: true
---
*[geometric-functions](geometric-functions) add (union)*

## syntax

- add(*polygon_data_itemA*, *polygon_data_itemB*)
- *polygon_data_itemA* + *polygon_data_itemB*

## description

add(*polygon_data_itemA*, *polygon_data_itemB*) or *polygon_data_itemA* + *polygon_data_itemB* results in a new multi [polygon](polygon) [data-item](data-item) with the **union** of the two *polygon_data_itemA* and *polygon_data_itemA* data items.

## applies to

data items *polygon_data_itemA* and *polygon_data_itemA* with an ipoint or spoint [value-type](value-type).

## conditions

1. The [composition](composition) of the [argument](argument) needs to be polygon.
2. The [domain-unit](domain-unit) of the arguments must match of be [void](void).

## since version

7.112

## example

<pre>
parameter&lt;ipoint&gt; NorthHolland (poly) := Land/geometry <B>+</B> Texel/geometry;
</pre>

## see also

- [union_polygon-(dissolve)](union_polygon-(dissolve))
- [add](add)