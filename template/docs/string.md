---
title: string
layout: default
nav_exclude: true
---
*[conversion-functions](conversion-functions) String*

## concept

- string is a string [value-type](value-type).
- string() is a function converting [data-item](data-item) or [unit](unit) of other value types to the string value type.

This page describes the string() function.

## syntax

- string(*a*)

## definition

- string(*a*) results in a **string** [data-item](data-item) converted from [tree-item](tree-item) *a*.

## applies to

- data item or unit with Numeric, uint2, uint4, or bool value type

## example

<pre>
attribute&lt;string&gt; stringA (ADomain) := <B>string(</B>A<B>)</B>;
</pre>

| A(int32) |**stringA**  |
|---------:|-------------|
| 0        | **'0**'     |
| 1        | **'1**'     |
| 256      | **'256**'   |
| -100     | **'-100**'  |
| 9999     | **'-9999**' |

*ADomain, nr of rows = 5*