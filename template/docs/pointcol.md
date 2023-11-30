---
title: pointcol
layout: default
nav_exclude: true
---
*[geometric-functions](geometric-functions) PointCol*

![](../assets/img/GUI/pointcol_function.png)

## syntax

- PointCol(*point data item*)

## definition

PointCol(*point data item*) results in a [data-item](data-item) with the **column numbers** of the *point data item* [point](point) data item.

_Be aware, the result is depending on the [xy-order](xy-order)._

## applies to

data item *point data item* with a Point [value-type](value-type)

## example

<pre>
attribute&lt;float32&gt; PointColXY (ADomain) := <B>PointCol(</B>pointXY<B>)</B>;
</pre>

| pointXY          | **PointColXY** |
|------------------|---------------:|
| {401331, 115135} | **115135**     |
| {399476, 111803} | **111803**     |
| {399289, 114903} | **114903**     |
| {401729, 111353} | **111353**     |
| {398696, 111741} | **111741**     |

*ADomain, nr of rows = 5*

## see also

- [pointrow](pointrow)