---
title: id
layout: default
nav_exclude: true
---
*[relational-functions](relational-functions) id*

## syntax

- id(*[domain-unit](domain-unit)*)

## definition

id(*domain unit*) results in an [attribute](attribute) with the [index-numbers](index-numbers) of the domain unit *domain unit*.

This *domain unit* argument is both domain unit and [values-unit](values-unit) of the resulting [attribute](attribute).

## description

An id(*domain unit*, [relation](relation)) function is not implemented. Use the [cumulate](cumulate) function to calculate index numbers per [partitioning](partitioning).

## applies to

- [unit](unit) with [value-type](value-type) of the group CanBedomain unit

## example

<pre>
unit&lt;uint32&gt; Region: NrofRows = 5;
attribute&lt;Region&gt; idRegion (Region) := <B>id(</B>Region<B>)</B>;
</pre>

| **idRegion** |
|-------------:|
| **0**        |
| **1**        |
| **2**        |
| **3**        |
| **4**        |

*domain Region, nr of rows = 5*