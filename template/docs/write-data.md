---
title: write-data
layout: default
nav_exclude: true
---
Data is written to a storage with a [storagemanager](storagemanager) if:

-   At least the StorageName [property](property) is configured to a [data-item](data-item) or it's [parent-item](parent-item). Often other StorageManager properties are also needed/useful.
-   The StorageManager supports writing data.
-   An [expression](expression) is configured for the data item, or derived from it's parent item.
-   The property [disablestorage](disablestorage) is not configured or set or set to false (default value).
-   The property [storagereadonly](storagereadonly) is not configured or set to false (default value).

The last two properties work hierarchical, if configured to a parent item they also apply to each of their [subitem](subitem). They can be overruled for specific subitems.

## example

<pre>
container WithContext
{
   template export
   {
      <I>// begin case parameters</I>
      parameter&lt;uint32&gt; n;
      <I>// end case parameters</I>

      unit&lt;uint32&gt; i := range(uint32, 0, n)
      ,  StorageName = "= '%LocalDataProjDir%' + PropValue(., 'FullName') + '/i.dbf'"
      {
         attribute&lt;uint32&gt;  sqr  := id(i) * id(i);
         attribute&lt;float64&gt; sqrt := sqrt(float64(sqr));
      }
   }
   container exports
   {
      container a := export(30);
      container b := export(40);
   }
}
</pre>

## file and folder

The StorageName property configures both folder as well as file name for the export. If the item for which the StorageName is configured is updated, the
resulting storage will be made. In the example a file i.dbf is written when item i is updated. The folder consists of two components:

-   %LocalDataProjDir%, a [folders-and-placeholders](folders-and-placeholders) referring to the LocalDataProjDir on your local machine
-   [propvalue](propvalue) (., 'FullName'), a context string referring to the full path of the parent of the item with the StorageName. By using this context     string, the resulting folder for the two case instantions will differ.

We advice to always configure both folder and file name. If no folder is configured, the storage will be written to your %ConfigDir%. If no file is configured, an error is generated.

Since GeoDMSVersion 7.140, it is also possible to add the _%configname%_ placeholder to your foldername.
This is useful if you project consists of multiple configurations (e.g. Vesta).