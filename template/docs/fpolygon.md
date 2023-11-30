---
title: fpolygon
layout: default
nav_exclude: true
---
*[conversion-functions](conversion-functions) fpolygon*

## syntax

- fpolygon(*a*)

## definition

fpolygon(*a*) converts the coordinates of a point [tree-item](tree-item) *a* with a sequence of points ([arc](arc) or [polygon](polygon)) to the **fpoint (float32 coordinates)** [value-type](value-type).

## applies to

- [data-item](data-item) with Point value type and [composition](composition) arc or polygon

## example

<pre>
attribute&lt;spoint&gt; fpolygonA (SDomain, polygon) := <B>fpolygon(</B>A<B>)</B>;
</pre>

| A(*fpolygon*)                                |**fpolygonA**                                     |
|----------------------------------------------|--------------------------------------------------|
| {2:{0,0},{1,1}}                              | **{2:{0,0},{1,1}}**                              |
| {3: {1E+007,1E+007},{-2.5,-2.5},{99.9,99.9}} | **{3: {1E+007,1E+007},{-2.5,-2.5},{99.9,99.9}}** |