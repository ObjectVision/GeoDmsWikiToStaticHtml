---
title: classify
layout: default
nav_exclude: true
---
*[classify-functions](classify-functions) classify*

## syntax

- classify(*a*, *ClassBreak*)

## definition

classify(*a*, *ClassBreak*) results in a **classified data item** with the [index-numbers](index-numbers) of the [domain-unit](domain-unit) of [data-item](data-item) ClassBreak. The resulting data item has the same domain unit as data item a.

## applies to

- *a*: numeric data item with Numeric [value-type](value-type) to be classified.
- *ClassBreak*: [data-item](data-item) with Numeric value type, used to classify the data. The ClassBreak data item contains the start value of each class. The end value of is derived from the ClassBreak value of the next class. The last class is always open.

## conditions

1. The [values-unit](values-unit) of [argument](argument) *a* and *ClassBreak* must match.

## example

<pre>
attribute&lt;m_5K&gt; classifyNrInh (DistrictDomain) := <B>classify(</B>NrInh, inh_4K/ClassBreaks<B>)</B>;
</pre>

| NrInh |ClassifyNrInh|
|------:|         ---:|
|550    |**2**        |
|1025   |**3**        |
|300    |**2**        |
|200    |**1**        |
|0      |**0**        |
|null   |**null**     |
|300    |**2**        |
|2      |**0**        |
|20     |**0**        |
|55     |**0**        |
|860    |**3**        |
|1025   |**3**        |
|1025   |**3**        |
|100    |**1**        |
|750    |**2**        |

*Table District, nr of rows = 15*;

| inh_4K/ClassBreaks |
|-------------------:|
| 0                  |
| 100                |
| 300                |
| 800                |

*Table inh_4K, nr of rows = 4*