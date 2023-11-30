---
title: pointrow
layout: default
nav_exclude: true
---
*[geometric-functions](geometric-functions) PointRow*

![](../assets/img/GUI/pointrow_function.png)

## syntax

- PointRow(*point data item*)

## definition

PointRow(*point data item*) results in a [data-item](data-item) with the **row numbers** of the *point data item* [point](point) data item.

_Be aware, the result is depending on the [xy-order](xy-order)._

## applies to

data item *point data item* with a Point [value-type](value-type)

## example

<pre>
attribute&lt;float32&gt; PointRowXY (ADomain) := <B>PointRow(</B>pointXY<B>)</B>;
</pre>

| pointXY          | **PointRowXY** |
|------------------|---------------:|
| {401331, 115135} | **401331**     |
| {399476, 111803} | **399476**     |
| {399289, 114903} | **399289**     |
| {401729, 111353} | **401729**     |
| {398696, 111741} | **398696**     |

*ADomain, nr of rows = 5*

## see also

- [pointcol](pointcol)