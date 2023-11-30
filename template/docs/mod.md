---
title: mod
layout: default
nav_exclude: true
---
*[arithmetic-functions](arithmetic-functions) modulo (%)*

## syntax

-   mod(*a*, *b*)
-   *a* % *b*

## definition

mod(*a*, *b*) or *a* % *b* is defined as *a* [**modulo**](https://en.wikipedia.org/wiki/Modulo_operation) *b*. The function results in the element-by-element remainder of division of the values of [data-item](data-item) *a* by the corresponding values of data item *b*.

## applies to

Data items with Numeric [value-type](value-type)

## conditions

1.  Domain unit of the [argument](argument) must match or be [void](void) ([literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)) or [parameter](parameter) can be calculated with data items of any domain).
2.  Arguments must have matching:
    -   [value-type](value-type)

## example

<pre>
1. attribute&lt;float32&gt; AmodB (ADomain) := <B>mod(</B>A, B<B>)</B>;
2. attribute&lt;float32&gt; AmodB (ADomain) := A <B>%</B> B;
</pre>

| A   | B   |**AmodB**|
|----:|----:|--------:|
| 0   | 1   | **0**   |
| 1   | 1   | **0**   |
| 4   | 2   | **0**   |
| 7   | 3   | **1**   |
| -5  | -2  | **-1**  |

*ADomain, nr of rows = 5*