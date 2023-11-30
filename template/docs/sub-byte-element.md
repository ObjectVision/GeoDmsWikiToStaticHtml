---
title: sub-byte-element
layout: default
nav_exclude: true
---
- Sub Byte Elements are values of type [bool](bool), [uint2](uint2), or [uint4](uint4), which require less than a byte for storage.
- All Sub Byte Elements are Unsigned (aka non-negative).
- Attributes store their values in arrays. Arrays of Sub Byte Elements are a multiple of 4 bytes long (DWORD) which each store 32 / NrOfBitsPerValue values per DWORD.
- All units of Sub Byte Element Values have a pre-defined cardinality of 2<sup>*NrBits*</sup>, which cannot be overridden, their first value is 0.
- There is no extra undefined value indicator for Sub Byte Elements.