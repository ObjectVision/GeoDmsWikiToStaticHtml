---
title: dist2
layout: default
nav_exclude: true
---
*[grid-functions](grid-functions) dist2*

## syntax

- dist2(*point_data_item*, *values unit*)

## definition

dist2(*point_data_item*, *values unit*) results in a new [attribute](attribute) of a [grid-domain](grid-domain) with the **distances** to the *point_data_item* [argument](argument).

The *values unit* argument is the [values-unit](values-unit) of the resulting attribute.

## description

The dist2 function is mainly used in the configuration of a [kernel](kernel), used for [potential](potential) calculations.

## applies to

- [data-item](data-item), usually a [parameter](parameter), *point_data_item* with Point [value-type](value-type)
- [unit](unit) *values unit* with numeric value type

## example

<pre>
unit&lt;spoint&gt; pot3Range: range = "[{-1, -1}, {2, 2})"
{
   attribute&lt;uint32&gt; distMatr := <B>dist2(</B>point(0s, 0s, pot3Range), uint32<B>)</B>;
};
</pre>
**pot3Range/distMatr**
|        |     |     | 
|-------:|----:|----:|
| **2**  |**1**|**2**|
| **1**  |**0**|**1**|
| **2**  |**1**|**2**|

*domain pot3Range, nr of rows = 3, nr of cols = 3*