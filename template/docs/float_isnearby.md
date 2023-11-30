---
title: float_isnearby
layout: default
nav_exclude: true
---
*[ordering-functions](ordering-functions) float_isNearby*

## syntax

- float_isNearby(*a*, *b*, *margin*)

## definition

float_isNearby(*a*, *b*, *margin*) results in a boolean [data-item](data-item) indicating if the values of data item *a* are **within the margin** *margin* of the corresponding values of data item *b*.

## description

With floating point data values, due to round offs, it can be useful to compare results and accept a margin in which the comparison still results in a True value. Use the float_isNearby function in stead of the [eq](eq) function in these cases.

The comparison between two missing values results in the value True.

The [point_isnearby](point_isnearby) function can be used in the similar manner as the float_isNearby function if the data items *a* and *b* are of a point [value-type](value-type).

## applies to

Data items *a*, *b*, *margin* with float32/64 value type

## conditions

1. [domain-unit](domain-unit) of the [argument](argument) must match or be [void](void) ([literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)%7Cliterals) or [parameter](parameter) can be compared to data items of any domain).
2. [argument](argument) must have matching:
   - [value-type](value-type)
   - [metric](metric) (only A and B)

## example

<pre>
attribute&lt;bool&gt; ANearByB (CDomain) := <B>float_isNearby(</B>A, B, 0.99f<B>)</B>;
</pre>

| A    | B     | **AisB**  |
|-----:|------:|-----------|
| 0    | 0     | **True**  |
| 1    | 2     | **False** |
| 2.5  | 2.49  | **True**  |
| -100 | -98   | **False** |
| 999  | 998.5 | **True**  |
| null | 0.1   | **False** |
| null | null  | **True**  |
| 0    | null  | **False** |
| null | 100   | **False** |
| 100  | null  | **False** |

*CDomain, nr of rows = 10*

## see also

- [eq](eq)