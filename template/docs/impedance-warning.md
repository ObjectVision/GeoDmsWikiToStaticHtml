---
title: impedance-warning
layout: default
nav_exclude: true
---
*[network-functions](network-functions) Impedance warning*

## memory and disk issues

The od variants of the Impedance functions result in a [domain-unit](domain-unit) that is a subset of the cartesian product of the origin and destination domain units, further: the set of od-pairs.

Be aware that this subset could be very large, causing memory and disk issues. Be aware of the [cardinality](cardinality) of the resulting domain unit when the result specification includes attributes of the set of od-pairs.

For full symmetric od matrices, keep the number of elements of the origin/destination domain units limited (we do have experience with domains of more than 10.000 elements, but calculation time and memory usage for the results increase with the number of od-pairs), use filters to cut the route search, or consider asymmetric variants with a lower number of origin zones. One could also try to avoid storing od-pair related attributes by using the results from available aggregations per origin and/or destination that can be updated during the processing of all destinations for each origin. See also https://github.com/ObjectVision/GeoDMS/issues/514

## see also

- [impedance-general-(formerly-known-as-dijkstra)](impedance-general-(formerly-known-as-dijkstra))
- [impedance-key-entities](impedance-key-entities)
- [impedance-functions](impedance-functions)
- [impedance-options](impedance-options)
- [impedance-interaction-potential](impedance-interaction-potential)
- [impedance-additional](impedance-additional)
- [impedance-future](impedance-future)
- [impedance-links](impedance-links)