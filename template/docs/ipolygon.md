---
title: ipolygon
layout: default
nav_exclude: true
---
*[conversion-functions](conversion-functions) ipolygon*

## syntax

- ipolygon(*a*)

## definition

ipolygon(*a*) converts the coordinates of a point [tree-item](tree-item) *a* with a sequence of points ([arc](arc) or [polygon](polygon)) to the **ipoint (int32 coordinates)** [value-type](value-type).

## applies to

- data item with Point value type and [composition](composition) [arc](arc) or [polygon](polygon)

## example

<pre>
attribute&lt;spoint&gt; ipolygonA (SDomain, polygon) := <B>ipolygon(</B>A<B>)</B>;
</pre>

| A(*fpolygon*)                                | **ipolygonA**                              |
|----------------------------------------------|--------------------------------------------|
| {2:{0,0},{1,1}}                              | **{2:{0,0},{1,1}}**                        |
| {3: {1E+007,1E+007},{-2.5,-2.5},{99.9,99.9}} | **{3: {9999999,9999999},{-2,-2},{99,99}}** |