---
title: storagename
layout: default
nav_exclude: true
---
The StorageName [property](property) needs to refer to the name of a primary data source (a file or database).

It can be configured to a [domain-unit](domain-unit), a [data-item](data-item) or [container](container), based on the [storagemanager](storagemanager).

Use placeholders in path names, like %SourceDataDir%, to make the configurations easily transferable to other locations/machines, see
[folders-and-placeholders](folders-and-placeholders).

For some StorageManagers, the file extension indicates which StorageManager will be used (.dbf, .shp, .tif). This can be overruled with the
[storagetype](storagetype) property.