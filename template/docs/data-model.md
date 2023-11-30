---
title: data-model
layout: default
nav_exclude: true
---
*[expression](expression) fast calculations: Data model*

## datamodel

-   [Memory](http://en.wikipedia.org/wiki/Random-access_memory)[Array](http://en.wikipedia.org/wiki/Array) based processing (as with [R](http://en.wikipedia.org/wiki/R_(programming_language)) and [IDL](http://en.wikipedia.org/wiki/IDL_(programming_language))). Computers are fast in calculating with arrays in internal memory. The GeoDMS uses this strentgh by calculating in this manner.
-   [Memory Mapped Files](http://msdn.microsoft.com/en-us/library/dd997372.aspx) utilizes the [paging](http://en.wikipedia.org/wiki/Paging) mechanism     to have data outside the working set standby without occupying [Virtual Address Space](http://en.wikipedia.org/wiki/Virtual_address_space).
-   SubByte [value-type](value-type) are supported. This means that in one [DWORD](http://en.wiktionary.org/wiki/dword), 32 booleans, 16 Uint2 values (of 2 bits each) or 8 Uint4 values (of 4 bits each) can be stored.
-   [Arrays](http://en.wikipedia.org/wiki/Array) of sequences (such as text strings, or polygons) are implemented as dual arrays (one index array and one element value array) to avoid [heap](http://en.wikipedia.org/wiki/Heap_(data_structure)) memory allocations per object.
-   Geometric data elements can also be configured with [single precision](http://en.wikipedia.org/wiki/Single_precision) (32 bit) floating point coordinates and 32 and 16 bits [integer](http://en.wikipedia.org/wiki/Integer) coordinates (both signed and unsigned) (most GIS software only support [double precision](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) coordinates.
-   Tiling (also known as Segmentation for non rasterdata) limits the use of the [Virtual Address Space](http://en.wikipedia.org/wiki/Virtual_address_space) (VAS) and divides calculations into smaller tasks. Large arrays are split up in multiple smaller arrays.
-   For most operations, type specific variants have been compiled that specialize operations for values with SubByte types, SequenceArrays, and the 6 point types for geometric values.