---
title: polygon
layout: default
nav_exclude: true
---
![](../assets/img/GUI/polygon_format.png)

Polygon [feature-attribute](feature-attribute) are [attribute](attribute) with a two-dimensional [value-type](value-type) (PointGroup) and **at least three coordinates** for each entry in the [domain-unit](domain-unit). The last coordinate need to be the same as the first coordinate (closed geometry).

Polygon attributes are used as feature attribute for [vector-data](vector-data). 

The points in the correct sequence define a [polygon](https://en.wikipedia.org/wiki/Polygon), a surface defined between a start point, one or more intermediates and an end point. The start point and end point need to be identical.

Polygon attributes are often used for [geography](geography) coordinates of regions, countries etc.

To make the GeoDMS aware that a sequence of coordinates need to be interpreted as an polygon, this is done by configuring the [composition](composition) to polygon.

## data model

In the GeoDMS data model a polygon is a sequence of points. The order of points in a sequence needs to be clockwise for exterior bounds (islands) and counter clockwise for holes in polygons (lakes).

For polygons with multiple rings (islands or holes), artificial lines are added between the rings, that are ignored when mapping the data in a mapview. But these artificial lines can effect [arc](arc) oriented functions like [arc_length](arc_length) and [connect_info](connect_info).

We advice to configure the [split_polygon](split_polygon) function first on polygons with multiple rings and apply arc oriented functions on the result of the split polygon.

## example

The polygon example a describes a data structure where each element in a domain unit is related to one or multiple polygon geometries. In these cases two domain units are necessary (such a structure could also apply to arcs):

<pre>
container administrative
{
   unit&lt;uint8&gt; province
   :  NrofRows   = 13
   ,  DialogData = "ProvinceShapes/prvnr"
   ,  DialogType = "Map"
   {
      attribute&lt;string&gt; label: 
         ['Abroad','Groningen','Friesland','Drenthe','Overijssel','Gelderland','Utrecht',
          'Noord-Holland','Zuid-Holland','Zeeland','Noord-Brabant','Limburg','Flevoland'];`
   }
   unit&lt;uint32&gt; ProvinceShape: StorageName = "%projDir%/data/Geography/prv.dbf"
   {
      attribute&lt;point_rd&gt; geometry (polygon) : StorageName = "%projDir%/data/Geography/prv.shp";
      attribute&lt;province&gt; prvnr;
   }
}
</pre>

The following two [domain-unit](domain-unit) are configured:

1.  The province unit is the domain unit of the administrative regions called provinces. The labels are configured for this domain unit as data item    in the configuration. The [dialogtype](dialogtype) is set to Map and the DialogData to the prvnr [relation](relation) referring to the ProvinceShapes domain unit.
2.  The ProvinceShape domain unit describes the total set of geometries/shapes. Some provinces like Friesland consist of multiple shapes (multiple islands). Therefore the number of elements of this ProvinceShape domain is larger than the number of elements of the province domain.

Each ProvinceShape element is related to one province. This relation, called prvnr is read from the .dbf file.

The feature attribute [geometry](geometry) is read from an [esri-shapefile](esri-shapefile) and has *polygon* configured as [composition](composition).

## see also
- [point](point)
- [arc](arc)
- [vector-data](vector-data)
- [grid-data](grid-data)
