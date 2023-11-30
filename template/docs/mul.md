---
title: mul
layout: default
nav_exclude: true
---
*[arithmetic-functions](arithmetic-functions) multiplication (*)*

## syntax

-   mul(*a*, *b*, ...)
-   *a* \* *b* \* ...

## definition

mul(*a*,*b*, ...) or *a* \* *b* \* ... results in the element-by-element [**multiplication**](http://en.wikipedia.org/wiki/Multiplication) of corresponding values of the [data-item](data-item): *a*, *b*, ...

If the result of the multiplication exceeds the MinValue or MaxValue of the [value type](https://github.com/ObjectVision/GeoDMS/wiki/Value-type), an error is generated. Use the [mul_or_null](mul_or_null) function if a [null](null) value is requested in these cases.

## applies to

Data items with Numeric or Point [value-type](value-type)

[unit](unit) with Numeric Value Type

## conditions

1.  [domain-unit](domain-unit) of the [argument](argument) must match or be [void](void) ([literals](http://en.wikipedia.org/wiki/Literal_(computer_programming)) or [parameter](parameter) can be added to data items of any domain).
2.  Arguments must have matching:
    -   [value-type](value-type)

## example

<pre>
1. attribute&lt;float32&gt; mulABC (ADomain) := <B>mul(</B>A, B, C<B>)</B>    
2. attribute&lt;float32&gt; mulABC (ADomain) := A <B>*</B> B <B>*</B> C;
</pre>

| A   | B    | C   | **mulABC**  | 
|----:|-----:|----:|------------:|
| 0   | 1    | 0   | **0**       |
| 1   | -1   | 1   | **-1**      |
| -2  | 2    | 4   | **-16**     |
| 3.6 | 1.44 | 7   | **36.29**   |
| 999 | 111  | -5  | **554,445** |

*ADomain, nr of rows = 5*

## see also
- [mul_or_null](mul_or_null)
- [mul-(overlap)](mul-(overlap))