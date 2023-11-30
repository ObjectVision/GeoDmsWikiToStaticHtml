---
title: add_or_null
layout: default
nav_exclude: true
---
*[arithmetic-functions](arithmetic-functions) add_or_null*

## syntax

-   add_or_null(*a, b*)

## definition

add_or_null(*a, b*) results in the element-by-element [**addition**](http://en.wikipedia.org/wiki/Addition) of corresponding values of the [data-item](data-item): *a* and *b*. If the result of the addition exceeds the MinValue or MaxValue of the [value-type](value-type), the add_or_null function results in the value [null](null).

## applies to

Data items with Numeric, Point, or String [value-type](value-type).

## conditions

1.  [domain-unit](domain-unit) of the [argument](argument) must match or be [void](void), ([literals](http://en.wikipedia.org/wiki/Literal_(computer_programming)) or [parameter](parameter) can be added to data items of any domain).
2.  Arguments must have matching:
    -   value type
    -   metric

## example

<pre>
1. attribute&lt;uint8&gt; add_or_null_AB (ADomain) := <B>add_or_null(</B>A, B<B>)</B>;
</pre>

| A   | B     | **add_or_null_AB**|
|----:|------:|------------------:|
|   0 |    1  |    **1**          |
|   1 | null  | **null**          |
| 200 |   54  | **254**           |
|  50 |  100  | **150**           |
| 222 |  111  | **null**          |

*ADomain, nr of rows = 5*

## see also

-   [add](add)