---
title: rescale
layout: default
nav_exclude: true
---
*[rescale-functions](rescale-functions) rescale*

## syntax

- rescale(*a*, *min*, *max*)

## definition

rescale(*a*, *min*, *max*) **scales** the [attribute](attribute) *a* **between** the [literal](https://en.wikipedia.org/wiki/Literal_(computer_programming)) / [parameter](parameter) ***min*** value and the literal / parameter ***max*** value.

The relative differences between the values in the new distribution are similar to the original distribution.

The resulting attribute has a new [values-unit](values-unit) and the same [domain-unit](domain-unit) as attribute *a*.

## description

To avoid rounding off errors in the rescale calculation, use a float32 of float64 [value-type](value-type) for the *a*, *min* and *max* [argument](argument).

Be cautious in using rescales. The values unit / [metric](metric) of the original attribute get's lost, less checks can be applied and the results become more difficult to interpret.

## conditions

The value type of attribute *a* and literal / parameter *min* and *max* must match.

## example

<pre>
attribute&lt;float32&gt; rescale_NrInh (City) := <B>rescale(</B>City/NrInhabitants, 0f, 1f<B>)</B>;
</pre>

| City/NrInhabitants | **rescale_nrInh** |
|-------------------:|------------------:|
| 550                | **1**             |
| 525                | **0.93**          |
| 300                | **0.33**          |
| 500                | **0.87**          |
| 200                | **0.07**          |
| 175                | **0**             |
| null               | **null**          |

*domain City, nr of rows = 7*