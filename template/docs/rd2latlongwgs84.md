---
title: rd2latlongwgs84
layout: default
nav_exclude: true
---
*[geometric-functions](geometric-functions) RD2LatLongWgs84*

## syntax

- RD2LatLongWgs84(*geometry*, *value type*)

## definition

RD2LatLongWgs84(*geometry*, *value type*) converts the [geometry](geometry) [argument](argument), expressed in the <B>[Dutch RD coordinate system](http://nl.wikipedia.org/wiki/RijksdriehoekscoB6rdinaten) towards the [Wgs84](http://en.wikipedia.org/wiki/World_Geodetic_System)
projection</B> of the [LatLong coordinate system](http://en.wikipedia.org/wiki/Geographic_coordinate_system).

The second optional argument is the *[value-type](value-type)* of the resulting [data-item](data-item).

## applies to

data item *geometry* with Point [value-type](value-type)

## since version

5.44

## example

<pre>
attribute&lt;dpoint&gt; district_LatLongWgs84 (DDomain, polygon) := <B>RD2LatLongWgs84(</B>district_rd, dpoint<B>)</B>;
</pre>

| district_rd             | **district_LatLongWgs84**           |
|-------------------------|-------------------------------------|
| {21: {403025, 113810}{4 | **{21: {51.6145901, 4.7924961}{51** |
| {17: {400990, 113269}{4 | **{17: {51.5962592, 4.7849284}{51** |
| {19: {401238, 115099}{4 | **{19: {51.5986213, 4.8113099}{51** |

*DDomain, nr of rows = 3*

## see also

- [latlongwgs842rd](latlongwgs842rd)
- [rd2latlongge](rd2latlongge)
- [rd2latlonged50](rd2latlonged50)
- [rd2latlong](rd2latlong)