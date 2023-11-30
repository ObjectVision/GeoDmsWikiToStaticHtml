---
title: data-item
layout: default
nav_exclude: true
---
The GeoDMS calculates and visualises data. Therefore [tree-item](tree-item) can to be configured, referring to source data or calculation results. These items are called **data items**.

From a technical perspective a data item is a reference to a [memory array](https://en.wikipedia.org/wiki/Array_data_structure).

[storagemanager](storagemanager) are used to read data from [files](https://en.wikipedia.org/wiki/Computer_file) and [databases](https://en.wikipedia.org/wiki/Database) into [memory arrays](https://en.wikipedia.org/wiki/Array_data_structure) and to write
data from these arrays to files.

Small amounts of data, like [parameter](parameter) values or class breaks of [classification](classification), are often
stored in [configuration-file](configuration-file).

Configure [expression](expression) to calculate with data items.

## types

Two types of data items are distinguished:

1.  [parameter](parameter)
2.  [attribute](attribute)

## multi-dimensional

Most data items are one-dimensional. The GeoDMS also supports the following multi-dimensional (spatial) datastructures:

1.  [point](point) data items: two-dimensional items with for each instance an X and an Y value.
2.  sequence of [point](point) data item: items with for each instance a non fixed number of coordinates, used for [arc](arc) and [polygon](polygon) data items.

Different [value-type](value-type) and [composition](composition) are used to configure multi-dimensional data structures, see [unit](unit). 