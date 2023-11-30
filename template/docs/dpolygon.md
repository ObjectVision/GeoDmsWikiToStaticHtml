---
title: dpolygon
layout: default
nav_exclude: true
---
*[conversion-functions](conversion-functions) dpolygon*

## syntax

- dpolygon(*a*)

## definition

dpolygon(*a*) converts the coordinates of a point [tree-item](tree-item) *a* with a sequence of points ([arc](arc) or [polygon](polygon)) to the **dpoint (float64 coordinates)** [value-type](value-type).

## applies to

- [data-item](data-item) with Point value type and [composition](composition) [arc](arc) or [polygon](polygon)

## example

<pre>
attribute&lt;spoint&gt; dpolygonA (SDomain, polygon) := <B>dpolygon(</B>A<B>)</B>;
</pre>

| A(*dpolygon*)                                | **dpolygonA**                                    |
|----------------------------------------------|--------------------------------------------------|
| {2:{0,0},{1,1}}                              | **{2:{0,0},{1,1}}**                              |
| {3: {1E+007,1E+007},{-2.5,-2.5},{99.9,99.9}} | **{3: {1E+007,1E+007},{-2.5,-2.5},{99.9,99.9}}** |