---
title: makedefined
layout: default
nav_exclude: true
---
*[predicates-functions](predicates-functions) MakeDefined*

## syntax

- MakeDefined(*a*, *value*)

## definition

MakeDefined(*a*, *value*) defines the [argument](argument) ***value* (often zero) for the [null](null)** values in [data-item](data-item) *a*.

## applies to

- data items with Numeric, Point or string [value-type](value-type)

## conditions

1. The [values-unit](values-unit) of the arguments *a* and *value* must match.
2. The [domain-unit](domain-unit) of the arguments must match or be [void](void) ([literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)) or [parameter](parameter) can be calculated with data items of any domain).

## example

<pre>
attribute&lt;float32&gt; MakeDefinedA (ADomain) := <B>MakeDefined(</B>A, 0f<B>)</B>;
</pre>

| A(float32) |**MakeDefinedA** |
|-----------:|----------------:|
| 0          | **0**           |
| null       | **0**           |
| 1000000    | **1000000**     |
| -2.5       | **-2.5**        |
| 99.9       | **99.9**        |

## see also

- [isdefined](isdefined)