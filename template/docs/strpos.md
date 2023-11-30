---
title: strpos
layout: default
nav_exclude: true
---
*[string-functions](string-functions) strpos(ition)*

## syntax

- strpos(*source*, *key*)

## description

The strpos(*source*, *key*) function results in the **character offset (position) of the first occurrence of** the *key* [argument](argument) value in the *source* argument, starting from the begin of the string value.

If no *key* value occurs as a substring in the *source* argument, the resulting value is [null](null).

The strpos function is [case sensitive](https://en.wikipedia.org/wiki/Case_sensitivity).

## condition

The [domain-unit](domain-unit) of both arguments must match or be [void](void) ([literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)) or [parameter](parameter) can be combined with [data-item](data-item) of any domain unit).

## example

<pre>
attribute&lt;uint32&gt; strposA (ADomain) := <B>strpos(</B>A, 't'<B>)</B>;
</pre>

| A                  | **strposA** |
|--------------------|-------------|
| 'Test'             |    **3**    |
| '88hallo99'        |    **null** |
| '+)'               |    **null** |
| 'twee woorden'     |    **0**    |
| ' test met spatie' |    **1**    |

*ADomain, nr of rows = 5*

## see also

- [strrpos](strrpos)