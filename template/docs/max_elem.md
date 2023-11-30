---
title: max_elem
layout: default
nav_exclude: true
---
*[ordering-functions](ordering-functions) maximum element*

## syntax

- max_elem(*a*, *b*, .. , *n*)

## definition

max_elem(*a*, *b*, .. , *n*) results in a [data-item](data-item) with the **highest value** of the [argument](argument) in the element-by-element comparison.

The [domain-unit](domain-unit) of the resulting item is the same as the domain units of all arguments of the function.

The [values-unit](values-unit) of the resulting item is the values unit of the of all arguments of the function.

## applies to

Data items with Numeric or string value type

## conditions

1. Domain of the arguments must match or be void.
2. Arguments must have matching:
    - [value-type](value-type)
    - [metric](metric)

## example

<pre>
attribute&lt;uint32&gt; max_elemABC (MDomain) := <B>max_elem(</B>A, B, C<B>)</B>;
</pre>

|A(int32)|B(int32)|C(int32)|max_elemABC|
|-------:|-------:|-------:|----------:|
|0       |1       |2       |**2**      |
|1       |-1      |4       |**4**      |
|-2      |2       |2       |**2**      |
|4       |0       |7       |**7**      |
|999     |111     |-5      |**999**    |
|2       |null    |1       |**0**      |
|0       |1       |null    |**0**      |
|null    |1       |2       |**0**      |
|null    |null    |null    |**null**   |

*MDomain, nr of rows = 9*

*In earlier versions (before 7.202) a null value in one of the arguments could result in a null value of the resulting data item. This now only occurs if all arguments have null values.*

## see also

- [max_elem_alldefined](max_elem_alldefined)
- [max_elem_ifdefined](max_elem_ifdefined)
- [min_elem](min_elem)
- [argmin](argmin)