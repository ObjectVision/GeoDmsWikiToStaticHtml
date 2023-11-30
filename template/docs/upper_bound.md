---
title: upper_bound
layout: default
nav_exclude: true
---
*[geometric-functions](geometric-functions) upper_bound*

## syntax

- upper_bound(*polygon_data_item*)

## definition

upper_bound(*polygon_data_item*) results in a [point](point) [data-item](data-item) with the **highest X and Y value** of the points in the *polygon_data_item*.

In the Dutch [RD coordinate system](https://nl.wikipedia.org/wiki/Rijksdriehoekscoördinaten), the upper_bound is the top right coordinate.

## applies to

data item *polygon_data_item* with fpoint or dpoint [value-type](value-type) and [composition](composition) polygon

## example

<pre>
attribute&lt;point_rd&gt; ub (district) := <B>upper_bound(</B>district/geometry<B>)</B>;
</pre>

| district/geometry      | **ub**               |
|------------------------|----------------------|
| {21 {403025, 113810}{4 | **{403552, 113810}** |
| {17 {400990, 113269}{4 | **{401597, 113291}** |
| {19 {401238, 115099}{4 | **{401642, 115164}** |

*domain district, nr of rows = 3*

## see also

- [lower_bound](lower_bound)
- [center_bound](center_bound)