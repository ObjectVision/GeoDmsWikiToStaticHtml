---
title: gt
layout: default
nav_exclude: true
---
*[ordering-functions](ordering-functions) greater than (>)*

## syntax

1. gt(*a*, *b*)
2. *a* > *b*

## definition

gt(*a*, *b*) or *a* \> *b* results in a boolean [data-item](data-item) indicating if the values of data item *a* are **greater than ** the corresponding values of data item *b*.

## description

Each comparison with missing values results in the value false.

## applies to

Data items with Numeric, string or bool [value-type](value-type)

## conditions

1. [domain-unit](domain-unit) of the [argument](argument) must match or be [void](void) ([literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)) or [parameter](parameter) can be compared to data items of any domain).
2. [argument](argument) must have matching:
    - [value-type](value-type)
    - [metric](metric)

## example

<pre>
1. attribute&lt;bool&gt; AgtB (CDomain) := <B>gt(</B>A, B<B>)</B>;
2. attribute&lt;bool&gt; AgtB (CDomain) := A <B>&gt;</B> B;
</pre>

| A    | B    | **AgeB**  |
|-----:|-----:|-----------|
| 0    | 0    | **False** |
| 1    | 2    | **False** |
| 2.5  | 2.5  | **False** |
| -100 | 100  | **False** |
| 999  | -999 | **True**  |
| null | 0    | **False** |
| null | null | **False** |
| 0    | null | **False** |
| null | 100  | **False** |
| 100  | null | **False** |

*CDomain, nr of rows = 10*

## see also

- [ge](ge)