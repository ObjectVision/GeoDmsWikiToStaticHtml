---
title: min_index
layout: default
nav_exclude: true
---
*[aggregation-functions](aggregation-functions) min_index*

## syntax

- min_index(*a*)
- min_index(*a*, *relation*)

## definition

- min_index(*a*) results in a [parameter](parameter) with the [index-numbers](index-numbers) of the **minimum** value of the non [null](null) values of [attribute](attribute) *a*.
- min_index(*a*, *relation*) results in an [attribute](attribute) with the index numbers of the **minimum** values of the non null values of attribute *a*, grouped by *[relation](relation)*. The [domain-unit](domain-unit) of the resulting attribute is the [values-unit](values-unit) of the *relation* attribute.

## description

The min_index function is not defined for string [data-item](data-item).

## applies to
- attribute *a* with Numeric, Point or boolean [value-type](value-type)
- *relation* with [value-type](value-type) of the group CanBeDomainUnit

## conditions

The [values-unit](values-unit) of the resulting data item should be the domain unit of [argument](argument) *a*.

## since version

7.184

## example

<pre>
parameter&lt;City&gt; min_index_NrInh                := <B>min_index(</B>City/NrInhabitants<B>)</B>; result = 5
attribute&lt;City&gt; min_index_NrInhRegion (Region) := <B>min_index(</B>City/NrInhabitants, City/Region_rel<B>)</B>;
</pre>

| City/NrInhabitants | City/Region_rel |
|-------------------:|----------------:|
| 550                | 0               |
| 525                | 1               |
| 300                | 2               |
| 500                | 1               |
| 200                | 3               |
| 175                | null            |
| null               | 3               |

*domain City, nr of rows = 7*

| **min_index_NrInhRegion** |
|--------------------------:|
| **0**                     |
| **3**                     |
| **2**                     |
| **4**                     |
| **null**                  |

*domain Region, nr of rows = 5*

## see also

- [max_index](max_index)
- [min](min)