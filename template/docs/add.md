---
title: add
layout: default
nav_exclude: true
---
*[arithmetic-functions](arithmetic-functions) addition (+)*

## syntax

-   add(*a, b, ...*) or add_list(*a, b, ...*)
-   *a* + *b* + ...

## definition

add(*a, b, ...*) or *a* + *b* + ... results in the element-by-element [**addition**](http://en.wikipedia.org/wiki/Addition) of corresponding values of the [data-item](data-item): *a*, *b*, ... .. 

add_list is a synonym for add

If the result of the addition exceeds the MinValue or MaxValue of the [value-type](value-type), an error is generated. Use the [add_or_null](add_or_null) function if a [null](null) value is requested in these cases.

## applies to

Data items with Numeric, Point, or String [value-type](value-type).

## conditions

1.  [domain-unit](domain-unit) of the [argument](argument) must match or be [void](void), ([literals](http://en.wikipedia.org/wiki/Literal_(computer_programming)) or [parameter](parameter) can be added to data items of any domain).
2.  Arguments must have matching:
    -   value type
    -   metric

## example

<pre>
1. attribute&lt;float32&gt; addABC (ADomain) := <B>add(</B>A, B, C<B>)</B>;
2. attribute&lt;float32&gt; addABC (ADomain) := A <B>+</B> B <B>+</B> C;
</pre>

| A   | B    | C   | **addABC**|
|----:|-----:|----:|----------:|
| 0   | 1    | 0   | **1**     |
| 1   | -1   | 1   | **1**     |
| -2  | 2    | 4   | **4**     |
| 3.6 | 1.44 | 7   | **12.04** |
| 999 | 111  | -5  | **1105**  |

*ADomain, nr of rows = 5*

## see also

- [add_or_null](add_or_null)
- [concatenation_(+)](concatenation_(+))
- [add-(union)](add-(union))
