---
title: roundup
layout: default
nav_exclude: true
---
*[conversion-functions](conversion-functions) roundUp*

## syntax

roundUp(*a*)

## definition

roundUp(*a*) results in a **integer data item rounded off upwards** from [data-item](data-item) *a*. Float32/64 data items are rounded off to the int32 [value-type](value-type), f/dpoint data items to the ipoint value type.

## applies to

- [data-item](data-item) with float32, float64, fpoint or dpoint [value-type](value-type)

## since version

5.45

## example

<pre>
attribute&lt;int32&gt; roundUpA (ADomain) := <B>roundUp(</B>A<B>)</B>;
</pre>

| A     |**roundUpA**|
|------:|-----------:|
| 1.49  | **2**      |
| 1.5   | **2**      |
| -1.49 | **-1**     |
| -1.5  | **-1**     |
| -1.51 | **-1**     |

*ADomain, nr of rows = 5*

## see also

- [roundup_64](roundup_64)
- [round](round)
- [rounddown](rounddown)
- [roundtozero](roundtozero)