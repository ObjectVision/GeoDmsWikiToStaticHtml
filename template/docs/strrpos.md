---
title: strrpos
layout: default
nav_exclude: true
---
*[string-functions](string-functions) strr(ight)pos(ition)*

## syntax

- strrpos(*source*, *key*)

## description

The strrpos(*source*, *key*) function results in the **character offset (position) of the first occurence of** the *key* [argument](argument) value in the *source* [argument](argument), **starting from the end of the string value**.

If no *key* value occurs as a substring in the *source* [argument](argument), the resulting value is [null](null).

The strrpos function is [case sensitive](https://en.wikipedia.org/wiki/Case_sensitivity).

## condition

The [domain-unit](domain-unit) of both arguments must match or be [void](void) ([literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)) or [parameter](parameter) can be combined with [data-item](data-item) of any domain unit).

## example

<pre>
attribute&lt;uint32&gt; strrposA (ADomain) := <B>strrpos(</B>A, 't'<B>)</B>;
</pre>

| A                  | **strposA** |
|--------------------|------------:|
| 'Test'             | **0**       |
| '88hallo99'        | **null**    |
| '+)'               | **null**    |
| 'twee woorden'     | **11**      |
| ' test met spatie' | **2**       |

*ADomain, nr of rows = 5*

## see also
- [strpos](strpos)