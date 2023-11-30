---
title: tablechopper-results
layout: default
nav_exclude: true
---
## results

An [ASCII file](https://en.wikipedia.org/wiki/ASCII) with the following data:

![](../assets/img/GUI/tablechopperfile.png)

is processed with the example [tablechopper-(read-ascii-file)](tablechopper-(read-ascii-file)) script, resulting in the following data items:

![](../assets/img/GUI/tablechoppertable.png)

With this ASCII file the **LinesAreSignedIntegerStringOrEmpy** [data-item](data-item) will result in True values for each row, except for the Corop area 2 (Delfzijl e.o) as this row contains floating point values.