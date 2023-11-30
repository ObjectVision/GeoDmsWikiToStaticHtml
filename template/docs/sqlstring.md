---
title: sqlstring
layout: default
nav_exclude: true
---
The SqlString property is used to specify which data and in which order will be selected from the database. The SqlString property requests a valid [SQL](https://nl.wikipedia.org/wiki/SQL) statement. It is used to:

-   Select the relevant [attribute](attribute). If the names in the database do not correspond with the [tree-item](tree-item) names use the AS keyword to relate these names.
-   Select the table(s), view(s)/query(ies) with a FROM clause
-   If needed, make a selection with a WHERE condition
-   Define the sort order with the ORDER BY. This is important, as if no ORDER BY clause is configured, the sort order of the records read is     undefined. As the GeoDMS calculates with arrays, the sequence is relevant. Therefor it is is important to always specify the ORDER BY clause in the SqlString property.

The SqlString property is used to select data. Use only the following SQL key words: SELECT, AS, FROM, WHERE and ORDER BY. If a SQL Statement with a JOIN or a GROUP BY is needed, define this as a view or query in the database and use it as source for the GeoDMS.

We advice to make complex selections, for instance with substrings, within the GeoDMS and not in the WHERE clause.

The SqlString property can not be used to modify data, UPDATE, SELECT INTO and DELETE statements are not allowed.

## Examples

### Example 1
```
unit<uint32> Read_Utrecht_gpkg_org
:	StorageName     = "%dataDir%/Plan_2022/Plan_openbaar_na_join.gpkg"
,	StorageType     = "gdal.vect"
,	StorageReadOnly = "true"
,	SqlString       = "SELECT * FROM Plan_openbaar_na_join WHERE status =='Hard' OR status =='Zacht' OR status =='Onbekend'";
```
### Example 2
```
container Import := for_each_nxs(rest_red/naam_underscore, uint32, rest_red/SqlString)
,	StorageName     = "%RSLDataDir%/Energie/RES/Analysekaarten/3_elektriciteit_aanbod_potentieel/wind/merge_wnd_hard_wt56_nat_ana_v3.gdb"
,	StorageReadOnly = "True"
,	SyncMode        = "Attr"
,	StorageType     = "gdal.vect"
,	SqlString       = "=rest_red/SqlString"
{
	unit<uint32> Beperkt_kwetsbare_gebouwen : sqlstring="SELECT * FROM merge_wnd_hard_wt56_nat_ana_v3 WHERE rest_red = 'Beperkt kwetsbare gebouwen'"
	{
		attribute<rdc_meter> geometry(poly);
	}
}
```

### Example 3
```
container Read_Roads_pbf
:	StorageName     = "= dir + '/'+Regio+'-'+date+'.osm.pbf'" 
,	StorageType     = "gdal.vect"
,	StorageReadOnly = "True"
, 	SyncMode        = "None"
, 	DialogData      = "wgs84"
{
	unit<uint32> multilinestrings : sqlstring = "SELECT * FROM multilinestrings"
	{
		attribute<wgs84>                        geometry (arc);
		attribute<string>                       other_tags;
	}
	unit<uint32> lines : sqlstring = "SELECT * FROM lines"
	{
		attribute<wgs84>                        geometry (arc);
		attribute<string>                       highway;
		attribute<string>                       other_tags;
		attribute<int32>                        z_order;
	}
}
```


