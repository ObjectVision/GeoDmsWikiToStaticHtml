---
title: geometry
layout: default
nav_exclude: true
---
The data item name: **geometry** is used as [naming-conventions](naming-conventions) for [feature-attribute](feature-attribute) of [vector-data](vector-data).

## origin

With [gdal.vect](gdal.vect), the geographic data is by default read with the name: geometry.

As gdal.vect is our advised [storagemanager](storagemanager) for vector data, we advice to use geometry as name for primary feature attributes of vector data.

## DialogType/DialogData

For vector data domains, the properties [dialogtype](dialogtype) and [dialogdata](dialogdata) are in use to make the GeoDMS aware of the feature attribute for the [domain-unit](domain-unit).

- The DialogType property is configured to *Map*
- The DialogData property is configured to the name of the feature attribute.

An advantage of naming the feature attribute geometry is that these [property](property) do not have to be configured anymore in recent versions of the GeoDMS. The feature attribute geometry needs to be a direct subitem of it's domain unit.