---
title: spoint
layout: default
nav_exclude: true
---
*[conversion-functions](conversion-functions) spoint*

## concept

1. spoint is a Point(Group) [value-type](value-type) with two coordinates of the 16 bits (2 bytes) signed integer value type: [int16](int16).
2. spoint() is a function converting other point [data-item](data-item) or [unit](unit) to the spoint [value-type](value-type).

This page describes the spoint() function.

## syntax

- spoint(*a*)

## definition

spoint(*a*) converts the coordinates of a point [tree-item](tree-item) *a* to the **spoint (int16 coordinates)** value type.

## applies to

- data item or unit with PointGroup [value-type](value-type)

## example

<pre>
attribute&lt;spoint&gt; spointA (ADomain) := <B>spoint(</B>A<B>)</B>;
</pre>

| A(*fpoint*)        | **spointA** |
|-------------------:|------------:|
| {0,0}              | **{0,0}**   |
| {1,1}              | **{1,1}**   |
| {1000000,10000000} | **null**    |
| {-2.5, 2.5}        | **{-2,2}**  |
| {99.9, 99.9}       | **{99,99}** |

*ADomain, nr of rows = 5*