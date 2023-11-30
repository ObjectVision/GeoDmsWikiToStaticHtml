---
title: sub_or_null
layout: default
nav_exclude: true
---
*[arithmetic-functions](arithmetic-functions) sub_or_null*

## syntax

- sub_or_null(*a, b*)

## definition

sub_or_null(*a, b*) results in the element-by-element [**subtraction**](http://en.wikipedia.org/wiki/Subtraction) of corresponding values of the [data-item](data-item): *a* and *b*. If the result of the addition exceeds the MinValue or MaxValue of the [value-type](value-type), the sub_or_null function results in the value [null](null).

## applies to

Data items with Numeric, Point, or String [value-type](value-type).

## conditions

1.  [domain-unit](domain-unit) of the [argument](argument) must match or be [void](void), ([literals](http://en.wikipedia.org/wiki/Literal_(computer_programming)) or [parameter](parameter) can be added to data items of any domain).
2.  Arguments must have matching:
    -   value type
    -   metric

## example

<pre>
1. attribute&lt;uint8&gt; sub_or_null_AB (ADomain) := <B>sub_or_null(</B>A, B<B>)</B>;
</pre>

| A   | B     | **sub_or_null_AB**|
|----:|------:|------------------:|
|   0 |    1  | **null**          |
|   1 | null  | **null**          |
| 200 |   54  | **146**           |
|  50 |  100  | **null**          |
| 222 |  111  | **111**           |

*ADomain, nr of rows = 5*

## see also

-   [sub](sub)