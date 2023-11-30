---
title: fss
layout: default
nav_exclude: true
---
The GeoDMS can read and write data from an own primary data format, called FSS, with the FSS [storagemanager](storagemanager). This format has the following advantages:

1.  It is a binary, fast format.
2.  It can store [vector-data](vector-data), [grid-data](grid-data) and non spatial data.
3.  It supports the hierarchical structures of GeoDMS configurations.
4.  It support both storing and reading [tile](tile).

The disadvantage of the format is that is is only supported by the GeoDMS. 
We therefore advice to use the FSS as exchange format between GeoDMS projects.

## example

### Writing FSS:

<pre>
unit&lt;uint32&gt; place := XML/woonplaats/ParsedXML/bag_LVC_Woonplaats
,   StorageName = "= FSSDir + '/place.fss'"
{
   attribute&lt;rdc_mm&gt; geom (polygon) := XML/woonplaats/geoBuilder/result;
   attribute&lt;string&gt; id             := bag_LVC_identificatie;
   attribute&lt;string&gt; name           := bag_LVC_woonplaatsNaam;
   container meta
   {
      attribute&lt;string&gt; status (..) := bag_LVC_woonplaatsStatus;
   }
}
</pre>
### Reading FSS:

<pre>
unit&lt;uint32> place
:   StorageName     = "= FSSDir + '/place.fss'"
,   StorageReadOnly = "True"
{
   attribute&lt;geometries/rdc_mm&gt; geom (polygon);
   attribute&lt;string&gt;            id;
   attribute&lt;string&gt;            name;

   container meta
   {
      attribute&lt;string&gt; status (..);
   }
}
</pre>
A FSS Storage always need to configured for a [unit](unit) as in the storage the number of entries is stored. Configuring a FSS for a container results in an error while reading the data.

The three [attribute](attribute) geom, id and name are stored as files with their name and .dmsdata extension in the woonplaats.fss folder (or with their name and a consecutive number in case of [tile](tile).

The attribute status is stored in a subfolder woonplaats.fss/meta. If data is stored in such subfolders, reading the data from the fss files requires this same hierarchy in your configuration (as in the example).

The [value-type](value-type) of the attribute read from the fss files need to match with the value type of the writing configuration script. Use this script to determine these value types and the hierarchy of the fss storage.

#### Reading FSS with a subfolder using a for each loop
<pre>
unit&lt;uint32&gt; place
: StorageName     = "= FSSDir + '/place.fss'"
, StorageReadOnly = "True"
{
  attribute&lt;geometries/rdc_mm&gt; geom (polygon);
  attribute&lt;string&gt;            id;
  attribute&lt;string&gt;            name;

  container meta :=
      for_each_ndv(
          status_types/name
         , place
         , string
      );
}
</pre>