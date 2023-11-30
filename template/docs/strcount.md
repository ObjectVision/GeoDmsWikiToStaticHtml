---
title: strcount
layout: default
nav_exclude: true
---
*[string-functions](string-functions) strcount*

## syntax

- strcount(*source*, *key*)

## definition

strcount(*source*, *key*) results in a uint32 [data-item](data-item) with the **number of occurences** of the substring *key* in the [argument](argument) *source*.

## description

The strcount function is [case sensitive](https://en.wikipedia.org/wiki/Case_sensitivity).

## applies to

data item *source* and *key* with string [value-type](value-type)

## conditions

The [domain-unit](domain-unit) of both [argument](argument) must match or be [void](void) ([literal](https://en.wikipedia.org/wiki/Literal_(computer_programming))s or [parameter](parameter) can be compared to data items of any domain unit).

## example

<pre>
attribute&lt;uint32&gt; strcountA (ADomain) := <B>strcount(</B>A, 't'<B>)</B>;
</pre>

| A                  |**strcountA** |
|--------------------|--------------|
| 'Test'             | **1**        |
| '88hallo99'        | **0**        |
| '+)'               | **0**        |
| 'twee woorden'     | **1**        |
| ' test met spatie' | **4**        |

*ADomain, nr of rows = 5*