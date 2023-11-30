---
title: tiled-domain
layout: default
nav_exclude: true
---
A tiled domain is a [domain-unit](domain-unit) with an additional [tiling](https://en.wikipedia.org/wiki/Tiled_rendering).

For one-dimensional domain units the word segmented is the synonym for a tiled domain.

A tiled domain can be configured with the [tiledunit](tiledunit) function.

Domain units with [value-type](value-type) of more that **2** bytes can be tiled, so:

- all Points Type value types: [spoint](spoint), [ipoint](ipoint), [wpoint](wpoint), [upoint](upoint)
- [uint32](uint32)
- [int32](int32)
- [uint64](uint64)
- [int64](int64)

thus not (u)int16, (u)int8, nor [uint4](uint4), [uint2](uint2) or [bool](bool) can be tiled.

## tiles as a set of Ranges

Each domain unit has a range of valid values, determined by the inclusive Lower Bound and exclusive Upper Bound.

For Point value types this result in a rectangular box of valid values.