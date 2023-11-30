---
title: convert
layout: default
nav_exclude: true
---
*[conversion-functions](conversion-functions) convert*

## definition

The convert function is a synonym for the [value](value) function.

## convert versus value function

The value function is usually used to define [values-unit](values-unit) for new [data-item](data-item), the convert function to convert data items to new related values units.

The concept of 'related' is in development. At the moment the convert function can be used to convert:
- related values units (like miles to meters) if based on the same [base-unit](base-unit)
- GDAL/PROJ4 reprojections for known projections

For future use also affine translations like conversions from degrees Celsius to Fahrenheit can be added to the convert function.

The convert function should <B>not</B> be used to convert data items with values units of unrelated [metric](metric), for instance to convert meters to second.
Use an [expression](expression) with an explicit multiplication factor (for instance 1 second per meter) for this purpose.