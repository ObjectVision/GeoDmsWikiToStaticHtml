---
title: atomicregionmap
layout: default
nav_exclude: true
---
*[allocation-functions](allocation-functions), argument 7: AtomicRegionMap*

## definition

*AtomicRegionMap* is the seventh [argument](argument) of the discrete_alloc function.

*AtomicRegionMap* is an [attribute](attribute) that defines **to which atomic region each land unit** belongs.

The [values-unit](values-unit) of this attribute must be the AtomicRegions [unit](unit), the [domain-unit](domain-unit) the LandUnitDomain unit.

## description

If the [overlay](overlay) function is used to derive a AtomicRegions unit, the resulting UnionData [subitem](subitem) of this function can be used as a base for an AtomicRegionMap, see the example.

The [lookup](lookup) operator is needed to relate the UnionData subitem to the LandUnitDomain for which the actual allocation is performed.

## applies to

attribute AtomicRegionMap with [value-type](value-type):

-   [uint8](uint8) or
-   [uint16](uint16)

## example
<pre>
unit&lt;uint8&gt; lu_type: nrofrows = 3
{ 
   attribute&lt;string> PartioningName: ['Living','Working','Nature'];
}
container regionSets
{
   attribute&lt;regMaps/p1&gt; Nature  (DomainGrid) := regMaps/p1Map;
   attribute&lt;regMaps/p1&gt; Living  (DomainGrid) := regMaps/p1Map;
   attribute&lt;regMaps/p2&gt; Working (DomainGrid) := regMaps/p2Map;
}

unit&lt;uint16&gt;             AtomicRegions             := overlay(lu_type/PartioningName, DomainGrid, regionSets);
attribute&lt;AtomicRegions&gt; AtomicRegionMap (ADomain) := AtomicRegions/UnionData[ADomain/nr_orgEntity];
</pre>