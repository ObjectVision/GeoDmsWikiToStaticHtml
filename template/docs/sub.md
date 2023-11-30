---
title: sub
layout: default
nav_exclude: true
---
*[arithmetic-functions](arithmetic-functions) subtract(-)*

## syntax

-   sub(*a, b*)
-   *a* - *b*

## definition

sub(*a*, *b*) or a - b results in the element-by-element [**subtraction**](http://en.wikipedia.org/wiki/Subtraction) of the values of [data-item](data-item) *b* from the corresponding values of data item *a*.

If the result of the subtraction exceeds the MinValue or MaxValue of the [value-type](value-type), an error is generated. Use the [sub_or_null](sub_or_null) function if a [null](null) value is requested in these cases.

## applies to

Data items with Numeric or Point [value-type](value-type)

## conditions

1.  [domain-unit](domain-unit) of the [argument](argument) must match or be [void](void) ([literals](http://en.wikipedia.org/wiki/Literal_(computer_programming)) or [parameter](parameter) can be subtracted from data items of any domain).
2.  [argument](argument) must have matching:
    -   [value-type](value-type)
    -   [metric](metric)

## example

<pre>
1. attribute&lt;float32&gt; AminB (ADomain) := <B>sub</B>(A, B);
2. attribute&lt;float32&gt; AminB (ADomain) := A <B>-</B> B;
</pre>

| A   | B    |**AminB** |
|----:|-----:|---------:|
| 0   | 1    | **-1**   |
| 1   | -1   | **2**    |
| -2  | 2    | **-4**   |
| 3.6 | 1.44 | **2.16** |
| 999 | 111  | **888**  |

*ADomain, nr of rows = 5*

## See also

- [sub_or_null](sub_or_null)
- [sub-(difference)](sub-(difference))
