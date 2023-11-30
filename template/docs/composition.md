---
title: composition
layout: default
nav_exclude: true
---
The composition type indicates how a sequence of coordinates need to be interpreted.

The GeoDMS supports two composition types:

1.  **arc**: an [arc](arc) consists of at least a start and end point and 0 or more intermediates per entry.
2.  **poly** or **polygon**: a [polygon](polygon) consist of at least three points per entry, the last and first point need to be the same to create a closed polygon. The composition type poly is also used to indicate multiple elements in [sequence-functions](sequence-functions).

The composition type is configured for [feature-attribute](feature-attribute) of arcs and polygons with the keyword **arc** or **polygon** in the same brackets as the [domain-unit](domain-unit). A comma separates domain units and the composition type, the order is irrelevant.

For [point](point) feature attributes no composition type has to be configured.