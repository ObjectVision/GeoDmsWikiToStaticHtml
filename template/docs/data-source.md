---
title: data-source
layout: default
parent: how-to-model
nav_order: 21
---
A typical workflow for a GeoDMS project is to
- [read-data](read-data) from a (set of) data source(s) (files/databases)
- calculate results in memory, using [arrays](https://en.wikipedia.org/wiki/Array_data_structure)
- view results and or [write-data](write-data) to files/databases.

To read data from and to write data to files/databases, so-called [storagemanager](storagemanager) are used.

We advise to configure source [data-item](data-item) in a source data container, these data items can be referred to from any other location in the configuration.

Data can also be explicitly exported with the [geodms-gui](geodms-gui) with the File > Export Primary Data menu options.

## vector, grid and non spatial data

For spatial data a distinction is made in:

-   [vector-data](vector-data): [point](point), [arc](arc) or [polygon](polygon) geometry data for [one-dimensional-domain](one-dimensional-domain)
-   [grid-data](grid-data): [attribute](attribute) for [two-dimensional-domain](two-dimensional-domain)

In [gdal](gdal) this same distinction is used, [gdal.vect](gdal.vect) or [gdalwrite.vect](gdalwrite.vect) is used for vector data, [gdal.grid](gdal.grid) or [gdalwrite.grid](gdalwrite.grid) for grid data.

Non spatial data can be also partly be read from or written to with gdal.vect or gdalwrite.vect but also by some other StorageManagers.