---
title: msaccess
layout: default
nav_exclude: true
---
## MsAccess Database

Example:
<pre>
container DataBase
:  StorageName  = "%projDir%/data/DB.mdb"
,  SyncMode     = "None"
{
   unit&lt;uint32> Table: SqlString = "SELECT * FROM TestTable ORDER BY ID"
   {
      attribute&lt;int32&gt;   IntegerAtt;
      attribute&lt;float32&gt; FloatAtt;
      attribute&lt;bool&gt;    BoolAtt;
      attribute&lt;string&gt;  StringAtt;
   }
}
</pre>
With the [storagename](storagename) property the database name is configured for the DataBase container. The GeoDMS recognises the .mdb extension as an MsAccess database and uses the [odbc](odbc) to read the data.

In the DataBase [container](container), [domain-unit](domain-unit) are configured for each relevant table and or view/query in the database. The number of elements of these units is derived from the number of records in the data source.