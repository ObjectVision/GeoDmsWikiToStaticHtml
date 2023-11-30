---
title: atomicregions
layout: default
nav_exclude: true
---
*[allocation-functions](allocation-functions), argument 6: AtomicRegions*

## definition

*AtomicRegions* is the sixth [argument](argument) of the discrete_alloc function.

*AtomicRegions* is a [domain-unit](domain-unit) defining the set of atomic regions.

It contains [attribute](attribute) for each *[partioningattribute](partioningattribute)* that define to which region each atomic region belongs for that *PartioningAttribute*.

## description

The overlay function is used to derive a *AtomicRegions* [unit](unit) with the set of relevant [subitem](subitem) for the discrete_alloc function, see the example.

## applies to

unit AtomicRegions with [value-type](value-type):
-   [uint8](uint8) or
-   [uint16](uint16)

## applies to

The names of the regions ([subitem](subitem) of the third argument of the [overlay](overlay) function need to match with the values of the [partioningname](partioningname) argument.

## example
<pre>
unit&lt;uint8&gt; lu_type: nrofrows = 3
{ 
   attribute&lt;string&gt; PartioningName: ['Living','Working','Nature'];
}
container regionSets
{
   attribute&lt;regMaps/p1&gt; Nature  (DomainGrid) := regMaps/p1Map;
   attribute&lt;regMaps/p1&gt; Living  (DomainGrid) := regMaps/p1Map;
   attribute&lt;regMaps/p2&gt; Working (DomainGrid) := regMaps/p2Map;
}
unit&lt;uint16&gt; AtomicRegions := overlay(lu_type/PartioningName, DomainGrid, regionSets);
</pre>
