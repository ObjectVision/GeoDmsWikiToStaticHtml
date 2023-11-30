---
title: unique
layout: default
nav_exclude: true
---
*[relational-functions](relational-functions) unique*

## syntax

- unique(*a*)

## definition

unique(*a*) results in a new uint32 [domain-unit](domain-unit) with the **unique occurences** of [attribute](attribute) *a*.

## description

The unique function generates a [subitem](subitem), named *Values*. This [data-item](data-item) contains the unique occurences of attribute *a*, sorted ascending.

The *Values* data item can be used in a [lookup](lookup) (in case attribute a is a relation) or a [rjoin](rjoin) function, to relate attributes to the new domain
unit, see the example.

## applies to

- attribute *a* with Numeric, Point, uint2, uint4, bool or string value type

## example

<pre>
unit&lt;uint32&gt; Region := <B>unique(</B>City/RegionCode<B>)</B>
{
   attribute&lt;string&gt; name := rjoin(Values, City/RegionCode, City/RegionName);
}
</pre>

| City/RegionCode | City/RegionName |
|----------------:|-----------------|
| 100             | Noord Holland   |
| 200             | Zuid Holland    |
| 300             | Utrecht         |
| 200             | Zuid Holland    |
| 400             | Noord Brabant   |
| null            | null            |
| 400             | null            |

*domain City, nr of rows = 7*

| **Region/Values** | Region/name   |
|------------------:|---------------|
| **100**           | Noord Holland |
| **200**           | Zuid Holland  |
| **300**           | Utrecht       |
| **400**           | Noord Brabant |
| **null**          | null          |

*domain <B>Region</B>, nr of rows = 5*

## see also

* [unique_uint8_16_32_64](unique_uint8_16_32_64)