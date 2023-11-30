---
title: eq
layout: default
nav_exclude: true
---
*[ordering-functions](ordering-functions) equals (==)*

## syntax

-   eq(*a*, *b*)
-   *a* == *b*

## definition

eq(*a*, *b*) or *a* ==*b* results in a boolean [data-item](data-item) indicating if the values of data item *a* are **equal to** the corresponding values of data item *b*.

## description

The comparison between two missing values ([null](null) == null) results in the value False.

## applies to

Data items with Numeric, Point, string or bool [value-type](value-type)

## conditions

1. [domain-unit](domain-unit) of the [argument](argument) must match or be [void](void) ([literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)%7Cliterals) or [parameter](parameter) can be compared to data items of any domain unit.
2. Arguments must have matching:
   - [value-type](value-type)
   - [metric](metric)

## example

<pre>
1. attribute&lt;bool&gt; AisB (CDomain) := <B>eq</B>(A, B);
2. attribute&lt;bool&gt; AisB (CDomain) := A <B>==</B> B;
</pre>

| A    | B    | **AisB**  |
|-----:|-----:|-----------|
| 0    | 0    | **True**  |
| 1    | 2    | **False** |
| 2.5  | 2.5  | **True**  |
| -100 | 100  | **False** |
| 999  | -999 | **False** |
| null | 0    | **False** |
| null | null | **False** |
| 0    | null | **False** |
| null | 100  | **False** |
| 100  | null | **False** |

*CDomain, nr of rows = 10*

## see also

- [eq_or_both_null](eq_or_both_null)
- [float_isnearby](float_isnearby)