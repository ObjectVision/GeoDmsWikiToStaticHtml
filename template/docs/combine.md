---
title: combine
layout: default
nav_exclude: true
---
*[relational-functions](relational-functions) combine*

## syntax

- combine(*a*, *b*, ... , *n*)

## definition

combine(*a*, *b*, ... , *n*) results in a uint32 [domain-unit](domain-unit) with the <B>[cartesian product](https://en.wikipedia.org/wiki/Cartesian_product)</B> of the domain units *a*, *b*, ..., *n*.

The number of elements of the new domain unit is the multiplication of the number of elements of *a*, *b*, ..., *n*.

## description

The combine function generates [subitem](subitem), named nr_SequenceNr, in the example *nr_1* for NHDomain and *nr_2* for YearDomain.

These [data-item](data-item) contain [relation](relation) to the original [domain-unit](domain-unit) and can be used in a [lookup](lookup) function to relate [attribute](attribute) to the new [domain-unit](domain-unit), see the example.

Use the [combine_data](combine_data) function to combine values of data items, resulting in a data item with the [unit](unit) resulting from the combine function as  [values-unit](values-unit).

Use a [combine_uint8_16_32_64](combine_uint8_16_32_64) function to configure a domain unit for another value type.

## applies to

- unit *a*, *b*, ..., *n* with value type from group CanBeDomainUnit

## conditions

The combine functions combines a maximum of six domain units. Use a combine in a combine if more domain units need to be combined.

## example

<pre>
unit&lt;uint32&gt; NHCityYear := <B>combine(</B>NHCity, YearDomain<B>)</B>
{ 
   attribute&lt;string&gt; NHCity_name := NHCity/name[nr_1];
   attribute&lt;string&gt; Year        := YearDomain/Year[nr_2];
}
</pre>

## see also

- [combine_uint8_16_32_64](combine_uint8_16_32_64)
- [combine_data](combine_data)