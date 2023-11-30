---
title: geometric-functions
layout: default
parent: operator
nav_order: 42
---
Geometric [operators-and-functions](operators-and-functions) calculate with geometries (coordinates) of [point](point), [arc](arc) or [polygon](polygon)

## point

- [point-function](point-function) - *make a point attribute based on an X and Y attribute*
- [point_isnearby](point_isnearby) - *compare if two points are (almost) the same location*
- [pointrow](pointrow) - *get the row numbers of a point attribute*
- [pointcol](pointcol) - *get the column numbers of a point attribute*
- [dist](dist) - *calculate the distance between two point sets*
- [sqrdist](sqrdist) - *calculate the square distance between two arrays of points*
- [bg_buffer_point](bg_buffer_point) - *creates a buffer polygon for each point in a pointset*

## polygon

- [area](area) - *calculates the surface of each polygon*
- [centroid](centroid) 
- [centroid_or_mid](centroid_or_mid) - *the centroid if it is located within a polygon or else a mid-point of a polygon.*
- [poly2grid](poly2grid) - *a grid representation of polygons*
- [poly2grid_untiled](poly2grid_untiled) - *a grid representation of polygons*
- [lower_bound](lower_bound) - *the lowest X and Y values of the points in each polygon*
- [upper_bound](upper_bound) - *the highest X and Y values of the points in each polygon*
- [center_bound](center_bound) - *the center X and Y values of the points in each polygon*
- [overlay_polygon-(intersect)](overlay_polygon-(intersect)) - *domain unit with the intersecting part of each polygon*
- [split_polygon](split_polygon) - *domain unit with all single polygons*
- [split_partitioned_union_polygon](split_partitioned_union_polygon) - *combination of [split_polygon](split_polygon) and [partitioned_union_polygon-(dissolve-by-attribute)](partitioned_union_polygon-(dissolve-by-attribute))*
- [polygon-inflated](polygon-inflated) - *increases each polygon*
- [polygon-deflated](polygon-deflated) - *decreases each polygon*
- [polygon_connectivity](polygon_connectivity) - *domain unit with the connected polygons*
- [sub-(difference)](sub-(difference)) - *a cutout of a polygon in another polygon*
- [mul-(overlap)](mul-(overlap)) - the *overlap of two arrays of polygons*
- [add-(union)](add-(union)) - *the element by element union of two polygons*
- [union_polygon-(dissolve)](union_polygon-(dissolve)) - *remove lines of adjacent polygons*
- [partitioned_union_polygon-(dissolve-by-attribute)](partitioned_union_polygon-(dissolve-by-attribute)) -  *remove lines of adjacent polygons, grouped by a relation*
- [bg_simplify_polygon](bg_simplify_polygon) - *simplify the geometry of a polygon*
- [bg_simplify_multi_polygon](bg_simplify_multi_polygon) - *simplify the geometry of a multi polygon*
- [bg_buffer_multi_polygon](bg_buffer_multi_polygon) - *creates a buffer polygon for each polygon*

_Several geometric polygon functions can be combined in a single operator; for the full list of those combinations see [polygon-processing-example](polygon-processing-example).

## points/arcs

- [dyna_point](dyna_point) / dyna_point_with_ends - *configures a point set for an arc on an equal distance*
- [dyna_segment](dyna_segment) / dyna_segments_with_ends - *configures a segment set for an arc on an equal distance*

## points/polygons

- [point_in_polygon](point_in_polygon) - *index number of the polygon in which a point is located*
- [point_in_ranked_polygon](point_in_ranked_polygon) - *index number of the polygon in which a point is located, using a ranking in case a polygon is located in multiple polygons*
- [point_in_all_polygons](point_in_all_polygons) - *relation between index numbers of the polygons in which points are located*
- [sequence2points](sequence2points) - *all vertices of each arc/polygon as separate points*
- [points2sequence](points2sequence) - *constructs arc/polygon from vertices*

## arc/polygon

- [arc_length](arc_length)
- [arc2segm](arc2segm) *- divides an arc/polygon data item into [segment](segment)*
- [bg_simplify_linestring](bg_simplify_linestring) - *simplifies the geometry of an arc*
- [bg_buffer_linestring](bg_buffer_linestring) - *creates a buffer polygon for each arc*
- [bg_buffer_multi_point](bg_buffer_multi_point)- *creates a buffer polygon for each coordinate of the arc/polygon*

## points/arcs/polygons

### conversion
- [rd2latlongwgs84](rd2latlongwgs84) - *converts coordinates from RD to LatLongWgs84*
- [latlongwgs842rd](latlongwgs842rd)- *converts coordinates from LatLongWgs84 to RD*
- [rd2latlongge](rd2latlongge)- *converts coordinates from RD to LatLongGE*
- [rd2latlonged50](rd2latlonged50)- *converts coordinates from RD to LatLongEd50*
- [rd2latlong](rd2latlong)- *converts coordinates from RD to LatLong*