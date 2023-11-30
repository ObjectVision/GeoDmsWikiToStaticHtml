---
title: lt
layout: default
nav_exclude: true
---
*[ordering-functions](ordering-functions) less than (\<)*

## syntax

1. lt(*a*, *b*)
2. *a* \< *b*

## definition

lt(*a*, *b*) or *a* \< *b* results in a boolean [data-item](data-item) indicating if the values of data item *a* are **less than** the corresponding values of data item *b*.

## description

Each comparison with missing values results in the value False.

## applies to

Data items with Numeric, string or bool [value-type](value-type)

## conditions

1. [domain-unit](domain-unit) of the [argument](argument) must match or be [void](void) ([literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)) or [parameter](parameter) can be compared to data items of any domain).
2. [argument](argument) must have matching:
    - [value-type](value-type)
    - [metric](metric)

## example

<pre>
1. attribute&lt;bool&gt; AltB (CDomain) := <B>lt(</B>A, B<B>)</B>;
2. attribute&lt;bool&gt; AltB (CDomain) := A <B>&lt;</B> B;
</pre>

| A    | B    | **AltB**  |
|-----:|-----:|-----------|
| 0    | 0    | **False** |
| 1    | 2    | **True**  |
| 2.5  | 2.5  | **False** |
| -100 | 100  | **True**  |
| 999  | -999 | **False** |
| null | 0    | **False** |
| null | null | **False** |
| 0    | null | **False** |
| null | 100  | **False** |
| 100  | null | **False** |

*CDomain, nr of rows = 10*

## see also

- [lt_or_lhs_null](lt_or_lhs_null)