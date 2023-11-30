---
title: upolygon
layout: default
nav_exclude: true
---
*[conversion-functions](conversion-functions) upolygon*

## syntax

- upolygon(*a*)

## definition

upolygon(*a*) converts the coordinates of a point [tree-item](tree-item) *a* with a sequence of points ([arc](arc) or [polygon](polygon)) to the **upoint (uint32 coordinates)** [value-type](value-type).

## applies to

- [data-item](data-item) with Point value type and [composition](composition) arc or polygon

## example

<pre>
attribute&lt;spoint&gt; upolygonA (SDomain, polygon) := <B>upolygon(</B>A<B>)</B>;
</pre>

| A(*fpolygon*)                                |**upolygonA**                                   |
|----------------------------------------------|------------------------------------------------|
| {2:{0,0},{1,1}}                              | **{2:{0,0},{1,1}}**                            |
| {3: {1E+007,1E+007},{-2.5,-2.5},{99.9,99.9}} | **{3: {9999999,9999999},{null,null},{99,99}}** |