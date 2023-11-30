---
title: unit
layout: default
parent: how-to-model
nav_order: 20
---
## data items and units

The GeoDMS calculates with [data-item](data-item). A data item represents a mapping between a [domain-unit](domain-unit) set and a value set. These sets are represented in the GeoDMS by unit items. For configured data items, the domain unit ([attribute](attribute) only) and [values-unit](values-unit) need to be configured
explicitly. The units are used to [unit-metric-consistency](unit-metric-consistency) in calculations.

Unit consistency checks are an important feature of the GeoDMS to improve the quality of models, as modelling errors are often related with incorrect use of units and related conversion factors. See also <http://en.wikipedia.org/wiki/Units_conversion_by_factor-label>.

For each [operators-and-functions](operators-and-functions) is defined if data of different units can be combined in a meaningful way.
The [add](add) operator can e.g. not meaningfully combine values expressed in meters with values expressed in seconds. These values can however be meaningfully combined with the [div](div) operator, resulting in a velocity attribute with values expressed in meter per second. More information on this topic can be found on the page [dimensional analysis](wikipedia:Dimensional_analysis "wikilink").

## syntax

Each unit is configured with the key word: unit. The [value-type](value-type) is indicated between the less than (\<) and greater than (>) characters, followed by the [tree-item-name](tree-item-name) of the unit e.g.

<pre>
unit&lt;uint32&gt; municipality2022: nrofrows = 335
</pre>

This results in a unit with 335 entries, to be used for all municipalities in 2022 in the Netherlands. 

## roles

A GeoDMS unit can have two roles:

1.  [domain-unit](domain-unit)
2.  [values-unit](values-unit)

This is similar to links forming a network by having an origin node and a destination node. The domain unit specifies the source of the mapping (entity) represented by a [data-item](data-item). The domain unit must be countable with a defined range (i.e. integer or a 2D rectangular integer rasterpointset or void). The values unit indicates in which value type and metric the values of a data items are expressed. 2D values (points, lines, polygons) can be a Projection, i.e. two affine translation of a basic coordinate System.

It is important to understand that the same unit can have multiple roles in one configuration. Assume we have a set of houses and a set of regions. The domain_unit house and region are configured, indicating the number of elements and order for the attributes of these domains. If we make a [relation](relation) which defines for each house in which region it is located, this would result in an attribute with as domain unit house and as values unit: region. So the unit region is used for both roles.

## element types

Elements can be:
-   one-dimensional
-   two-dimensional
-   a single value
-   sequence of values

The values can be (un)signed, integer or float, or text-string (implemented as a sequence of characters).

Each element has a value type that determines how its value(s) is/are represented in memory and which determines its minimum and maximum value and its granularity. [operators-and-functions](operators-and-functions) are implemented to operate on data items of (combinations of) value types.

Usually, different combinations are dealt with by different instantiations of an operator/function, to avoid time on processing value type conversion or larger than required memory-footprints. With [conversion-functions](conversion-functions), data items can be converted to other values units and value types.