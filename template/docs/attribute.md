---
title: attribute
layout: default
nav_exclude: true
---
Attributes are data items|data_item]] referring to [arrays of data values](https://en.wikipedia.org/wiki/Array_data_structure).
Conceptually attributes are characteristics of an [entity](https://en.wiktionary.org/wiki/entity), think about a column in a table.

In the GeoDMS this means that each attribute belongs to such a table, the so-called [domain-unit](domain-unit).

## syntax

- Start with the keyword: **attribute**
- Configure between the less than (\<) and greater than (>) characters it's [values-unit](values-unit).
- Next configure the [tree-item-name](tree-item-name) of the parameter.
- Configure between normal brackets it's domain unit.
- For attributes often configured [expression](expression) are configured but also other [property](property) can be configured.
- To finalize the definition of an item, configure a [semicolon (;)](https://en.wikipedia.org/wiki/Semicolon) character.

## example

```
attribute<hectare> building (grid_500m) := residential + utility;
```

The example configures an attribute called building. The values are expressed in hectares, so hectare is configured as values unit.

The domain unit for this attribute is grid_500m, defining a grid with cells of 500 * 500 meter.

The attribute results are calculated with an expression, buildings is defined as the sum of residential and utility.