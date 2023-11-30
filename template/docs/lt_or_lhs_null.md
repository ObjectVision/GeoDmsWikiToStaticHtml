---
title: lt_or_lhs_null
layout: default
nav_exclude: true
---
*[ordering-functions](ordering-functions) less than or left side has null values*

## syntax

- lt_or_lhs_null(*a*,*b*)

## definition

lt_or_lhs_null(*a*, *b*) results in a boolean [data-item](data-item) indicating if the values of data item *a* are **less than** the corresponding values of data item *b* or if the **values of data item *a* are [null](null)**.

## description

The comparison with missing values in data item a results in the value True (except for null values in data item *b*).

## applies to

Data items with Numeric, string or bool [value-type](value-type)

## conditions

1. [domain-unit](domain-unit) of the [argument](argument) must match or be [void](void) ([literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)) or [parameter](parameter) can be compared to data items of any domain).
2. [argument](argument) must have matching:
    - [value-type](value-type)
    - [metric](metric)

## example

<pre>
attribute&lt;bool&gt; AltB (CDomain) := <B>lt_or_lhs_null(</B>A, B<B>)</B>;
</pre>

| A    | B    | **AltB**  |
|-----:|-----:|-----------|
| 0    | 0    | **False** |
| 1    | 2    | **True**  |
| 2.5  | 2.5  | **False** |
| -100 | 100  | **True**  |
| 999  | -999 | **False** |
| null | 0    | **True**  |
| null | null | **False** |
| 0    | null | **False** |
| null | 100  | **True**  |
| 100  | null | **False** |

*CDomain, nr of rows = 10*

## see also

- [lt](lt)