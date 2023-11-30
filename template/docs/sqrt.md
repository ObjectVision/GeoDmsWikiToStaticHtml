---
title: sqrt
layout: default
nav_exclude: true
---
*[arithmetic-functions](arithmetic-functions) square root (√a)*

## syntax

-   sqrt(*a*)

## definition

sqrt(*a*) results in the [*square root*](https://en.wikipedia.org/wiki/Square_root) of the values of [data-item](data-item) *a*, synonym with √*a*.

## description

The sqrt function results in null values for negative values in the [argument](argument).

## applies to

data item or [unit](unit) with Numeric [value-type](value-type)

## example

<pre>
attribute&lt;float32&gt; sqrtA (ADomain) := <B>sqrt(</B>A<B>)</B>;
</pre>

| A   |**sqrtA**  |
|----:|----------:|
| 0   | **0**     |
| 1   | **1**     |
| -2  | **null**  |
| 3.6 | **1.897** |
| 999 | **31.6**  |

*ADomain, nr of rows = 5*