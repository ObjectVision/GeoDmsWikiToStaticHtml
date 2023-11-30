---
title: isdefined
layout: default
nav_exclude: true
---
*[predicates-functions](predicates-functions) IsDefined*

## syntax

- IsDefined(*a*)

## definition

IsDefined(*a*) results in a boolean [data-item](data-item) with values **True for non [null](null) and False for null values** of data item *a*.

## applies to

- data item with Numeric, Point or string [value-type](value-type)

## example

<pre>
attribute&lt;bool&gt; IsDefinedA (ADomain) := <B>IsDefined(</B>A<B>)</B>;
</pre>

| A(float32) |**IsDefinedA** |
|-----------:|---------------|
| 0          | **True**      |
| null       | **False**     |
| 1000000    | **True**      |
| -2.5       | **True**      |
| 99.9       | **True**      |

*ADomain, nr of rows = 5*

## see also

- [makedefined](makedefined)
- [isnull](isnull)