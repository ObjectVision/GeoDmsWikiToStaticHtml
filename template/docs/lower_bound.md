---
title: lower_bound
layout: default
nav_exclude: true
---
*[geometric-functions](geometric-functions) lower_bound*

## syntax

- lower_bound(*polygon_data_item*)

## definition

lower_bound(*polygon_data_item*) results in a [point](point) [data-item](data-item) with the **lowest X and Y value** of the points in the *polygon_data_item*.

In the Dutch [RD coordinate system](https://nl.wikipedia.org/wiki/Rijksdriehoekscoördinaten), the lower_bound is the bottom left coordinate.

## applies to

data item *polygon_data_item* with fpoint or dpoint [value-type](value-type) and [composition](composition) polygon

## example
<pre>
attribute&lt;point_rd&gt; lb (district) := <B>lower_bound(</B>district/geometry<B>)</B>;
</pre>

| district/geometry      | **lb**               |
|------------------------|----------------------|
| {21 {403025, 113810}{4 | **{402428, 112312}** |
| {17 {400990, 113269}{4 | **{400817, 112176}** |
| {19 {401238, 115099}{4 | **{400888, 112888}** |

*domain district, nr of rows = 3*

## see also

- [upper_bound](upper_bound)
- [center_bound](center_bound)