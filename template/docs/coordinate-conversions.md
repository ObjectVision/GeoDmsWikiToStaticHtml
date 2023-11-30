---
title: coordinate-conversions
layout: default
nav_exclude: true
---
Coordinates in the GeoDMS can be converted between and within [coordinate-system](coordinate-system). This can be useful if:
- your source data uses different coordinates as your project
- you want to convert vector data to grids or vice versa 
- your coordinates need to be converted to integer coordinates for polygon operations
- your want to [simplify your geometry](https://strk.kbt.io/blog/2012/04/13/simplifying-a-map-layer-using-postgis-topology/)

## between different coordinate systems

There are two options to convert [vector-data](vector-data) between different coordinate systems:
1. [geometric functions](https://github.com/ObjectVision/GeoDMS/wiki/Geometric-functions#conversion) are available to convert e.g. [Rijksdriehoekcoördinaten](https://nl.wikipedia.org/wiki/Rijksdriehoeksco%C3%B6rdinaten) to LatLongWgs84 coordinates. 
2. Use configured [EPSG codes](https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset):

<pre>
unit&lt;upoint&gt; rdc_base   : SpatialReference = "EPSG:28992";
unit&lt;dpoint&gt; wgs84_base : SpatialReference = "EPSG:4326";

parameter&lt;rdc_base&gt;    rdc_point   := point(390390, 111612, rdc_base);
parameter&lt;wgs84_base&gt; wgs84_point := convert(rdc_point, wgs84_base);
</pre>

_Until 8.7.0 the format property was used instead of SpatialReference._

## conversions within a coordinate system

### vector data to grid and vice versa

See [point-2-grid](point-2-grid) and [grid-2-point](grid-2-point) examples for how to convert [vector-data](vector-data) to [grid-data](grid-data) and vice versa.

### vector data expressed in different [values-unit](values-unit)

conversions within a coordinate system, for instance to integer coordinates or from meter to hectometer can be configured in two steps:

1) configure the new [values-unit](values-unit) with an [expression](expression) relating to the original values unit.
2) relate the coordinates with the [value](value) function

See the following example (default order of Y, X in point functions, see [XY order](https://github.com/ObjectVision/GeoDMS/wiki/XY-order)):
<pre>
unit&lt;float32&gt; m               := baseunit('m', float32), label = "meter";
unit&lt;fpoint&gt;  point_rd_base   : SpatialReference = "EPSG:28992";
unit&lt;fpoint&gt;  point_rd        := range(point_rd_base, point(300000[m],0[m]), point(625000[m],280000[m]));
unit&lt;ipoint&gt;  point_rd_ipoint := ipoint(point_rd);
unit&lt;ipoint&gt;  point_rd_hectom := <I>//values unit for rijkdsriehoek coordinates in hectometers</I>
  gridset(point_rd, point(100f, 100f, point_rd), point(0f, 0f, point_rd), ipoint);

attribute&lt;point_rd&gt;        geometry        (DomainUnit, polygon);
attribute&lt;point_rd_ipoint&gt; geometry_ipoint (DomainUnit, polygon) := geometry[point_rd_ipoint];
attribute&lt;point_rd_hectom&gt; geometry_hectom (DomainUnit, polygon) := geometry[point_rd_hectom];
</pre>

The point_rd_ipoint && point_rd_hectom values units are configured based on the base unit of this coordinate system: point_rd (in meters).

The geometry_ipoint [attribute](attribute) results in an integer variant of the geometry coordinates. The geometry_hectom attribute results in coordinates in hectometer.

## conversion issues

For [polygon](polygon), converting coordinates might result in unexpected lines in the visualisation, see the next example:

![](../assets/img/GUI/convertcoordinatesissue.png)

This is related to the polygon data model, using artificial lines between rings. This issue can be solved by [clean-polygon-geometry](clean-polygon-geometry).

## see also

- [coordinate-system](coordinate-system)
- [how-to-configure-a-coordinate-system](how-to-configure-a-coordinate-system)