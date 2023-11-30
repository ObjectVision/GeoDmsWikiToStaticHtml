---
title: storagemanager
layout: default
nav_exclude: true
---
A StorageManager is part of the GeoDMS software used to read or write data from and to files or databases.

If a StorageManager is configured, data is

- [read-data](read-data) the storage when requested in a view or calculation.
- [write-data](write-data) the storage when a [data-item](data-item) is updated (results of the [expression](expression) are calculated).

Requesting data in a view triggers the GeoDMS to update items, as well as the submenu items Update Treeitem and Update Subtree in the [geodms-gui](geodms-gui).

Since 6.045 (read) and 7.408 (write) we use the [gdal](gdal) library to read data from and write data to multiple formats, additional to the GeoDMS StorageManagers that are also still useful in specific cases.

## example

The following example show the configuration of the [dbf](dbf) StorageManager for reading data form a _region.dbf_ file.  

<pre>
unit&lt;uint32&gt; Table
:   StorageName     = "%SourceDataDir%/CBS/region.dbf"
,   StorageType     = "dbf"
,   Source          = "dbf example source"
,   StorageReadOnly = "True"
,   SyncMode        = "None"
,   SqlString       = "SELECT * FROM TestTable ORDER BY ID"
{
     attribute&lt;int32&gt; att;
     attribute&lt;int32&gt; att2 := att * att, DisableStorage = "True";          `
}
</pre>

## properties

A StorageManager is configured by setting [property](property) to a data item or it's [parent-item](parent-item).

-   [storagename](storagename)
-   [storagetype](storagetype)
-   [source](source)
-   [storagereadonly](storagereadonly)
-   [disablestorage](disablestorage)
-   [syncmode](syncmode)
-   [sqlstring](sqlstring)

## formats

-   [vector-data](vector-data) ([esri-shapefile](esri-shapefile))
-   [grid-data](grid-data) ([geotiff](geotiff), ...)
-   [ascii-files](ascii-files) ([csv](csv))
-   [xml](xml)
-   [dbf](dbf)
-   [database](database) ([geopackage](geopackage))
-   [geodms-own-formats](geodms-own-formats)