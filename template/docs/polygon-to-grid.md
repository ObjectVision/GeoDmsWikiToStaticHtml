---
title: polygon-to-grid
layout: default
nav_exclude: true
---
*[configuration-examples](configuration-examples) Polygon to grid*

This example is used to read an [attribute](attribute) from a [polygon](polygon) [esri-shapefile](esri-shapefile), make a [relation](relation) from the polygons to a [grid](grid) and calculate the attribute for the [grid-domain](grid-domain).

## example
<pre>
unit&lt;uint16&gt; earthquake
:  StorageName      = "%SourceDataDir%/physics/earthquakes.shp"
,  StorageType      = "gdal.vect"
,  StorageReadOnly  = "True"
{
   attribute&lt;LatLong&gt; geometry (polygon); <I>// LatLong must be the coordinate system unit</I>
   attribute&lt;int32&gt;   zone;               <I>
   // HeatOption must be an attribute in the dbf file accompanying the shp file </I>
}

attribute&lt;earthquake&gt; earthquake_rel (gtopo) := poly2grid(earthquake/geometry, gtopo); <I>
  // gtopo must be the grid domain unit referring to the LatLong coordinate system unit </I>
attribute&lt;int32&gt;      zone           (gtopo) := earthquake/zone[earthquake_rel];
</pre>