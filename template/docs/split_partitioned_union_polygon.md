---
title: split_partitioned_union_polygon
layout: default
nav_exclude: true
---
*[geometric-functions](geometric-functions) split_partitioned_union_polygon*

## syntax

- split_partitioned_union_polygon(*polygon_data_item*, *relation*)

## description

split_partitioned_union_polygon(polygon_data_item, relation) results in a new uint32 [domain-unit](domain-unit) with **single polygons** for each (multi)[polygon](polygon) in the *polygon_data_item* [argument](argument), and also dissolves over the relation.

## applies to

attribute *polygon_data_item* with an ipoint or spoint [value-type](value-type)

## conditions

1. The [composition](composition) of the *polygon_data_item* argument needs to be polygon.
2. The domain unit of the *polygon_data_item* [argument](argument) must be of value type uint32.

## since version

7.042

## example

```
unit<uint32> split_dissolve := split_partitioned_union_polygon(multipolygon/geometry, id(multipolygon))
```

## see also
- [union_polygon-(dissolve)](union_polygon-(dissolve))