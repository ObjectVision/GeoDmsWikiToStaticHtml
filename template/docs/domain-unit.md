---
title: domain-unit
layout: default
nav_exclude: true
---
A domain unit defines the [entity](https://en.wiktionary.org/wiki/entity) to which an [attribute](attribute) belongs.

Different domain unit types are:

- [geography](geography) like: Country, Nuts2 region, 1km grid cell.
- Model object like house, service, street. The data is often read from an external [data-source](data-source) (database or file).
- [classification](classification) like Corine, EHS, Percentage_10K, often configured as domain unit of a Classification Scheme.

The GeoDMS supports both [one-dimensional-domain](one-dimensional-domain) and [two-dimensional-domain](two-dimensional-domain) domains. The [value-type](value-type) of the domain unit defines the number of dimensions and the [cardinality](cardinality). The allowed value types for domain units can be found in the CanBeDomain column of the value type table.

## tiled/segmented Data

For tiled/segmented data, a tiled domain unit is needed. A tiled domain is a domain with an additional tiling/segmenting. Only domains with value types of more that 2 bytes (all point value types, uint32, int32, uint64 or int64) can be tiled/segmented.

## configuration

See [domain-unit-example](domain-unit-example) for how to configure domain units.