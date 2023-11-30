---
title: gdal
layout: default
nav_exclude: true
---
Since version 6.045 The GeoDMS includes the [GDAL](https://en.wikipedia.org/wiki/GDAL) library as a [storagemanager](storagemanager) collection to read multiple (spatial) data formats.

Since version 7.400, GeoDMS uses GDAL 3 (regular updates, with [Microsoft's vcpkg package manager](https://vcpkg.io/en/packages.html)). Data can now both be read from as well as written to (from version 7.408) data sources with GDAL.   

## formats

GDAL support the following [raster](https://gdal.org/drivers/raster/) and [vector](https://gdal.org/drivers/vector/) drivers.

The following table shows which formats are tested/documented. Other formats may also work, but are not (yet) supported.
The second and third column indicates which StorageType to use for the format.

| format                                | read          | write              |
|---------------------------------------|---------------|--------------------|
| [csv](csv)                               | [gdal.vect](gdal.vect) | [gdalwrite.vect](gdalwrite.vect) |
| [dbf](dbf)                               | [gdal.vect](gdal.vect) | [gdalwrite.vect](gdalwrite.vect) |
| [esri-shapefile](esri-shapefile) (point, arc, poly) | [gdal.vect](gdal.vect) | [gdalwrite.vect](gdalwrite.vect) |
| [geopackage](geopackage)                        | [gdal.vect](gdal.vect) | [gdalwrite.vect](gdalwrite.vect) |
| GeoJSON                               | [gdal.vect](gdal.vect) | [gdalwrite.vect](gdalwrite.vect) |
| gml                                   | [gdal.vect](gdal.vect) | [gdalwrite.vect](gdalwrite.vect) |
| [filegeodatabase](filegeodatabase)                   | [gdal.vect](gdal.vect) |                    |
| [pbf-(osm)](pbf-(osm))                         | [gdal.vect](gdal.vect) |                    |
| [geotiff](geotiff)                           | [gdal.grid](gdal.grid) | [gdalwrite.grid](gdalwrite.grid) |


### driver selection

As it is possible to read multiple data formats with GDAL, a specific driver needs to be chosen to open a dataset.

The default behavior is that GDAL tries to open the dataset based on the the file/database extension. The first driver that successfully manages to open the given dataset is used for further reading. It is possible to overrule this driver, e.g. if you want to open a dataset specifically with the netCDF driver use:

<pre>
parameter&lt;string&gt; GDAL_Driver : ['netCDF'];
</pre>

### options
There are various driver specific [gdal-options](gdal-options) available to modify the behavior of a driver. 

### development
As GDAL (especially GDAL3 and writing data with GDAL) is relatively new, there might be some issues. See [gdal-update-issues](gdal-update-issues) for the latest information.      


