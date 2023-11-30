---
title: getprojectionfactor
layout: default
nav_exclude: true
---
*[unit-functions](unit-functions) GetProjectionFactor*

## syntax

- *GetProjectionFactor(*gridunit*)*

## definition

GetProjectionFactor(*gridunit*) results in a [parameter](parameter) with a dpoint [value-type](value-type), indicating the gridsize in both X and Y directions.

The grid size is expressed in the [unit](unit) of the [grid-domain](grid-domain).

## description

The GetProjectionFactor function in combination with the [getprojectionfactor](getprojectionfactor) function was used to calculate [grid](grid) [relation](relation) for a set of points.

Since GeoDMS version 7.015 this is done with the [value](value) function, see [configuration-examples](configuration-examples) Grid.

## applies to

- unit *gridunit* with Point value type of the group CanBeDomainUnit

## since version

5.44

## example

<pre>
unit&lt;fpoint&gt; rdc_meter: range = "[{300000, 0}, {625000, 280000})";
unit&lt;spoint&gt; rdc_100 :=
   range(
      gridset(
          rdc_meter
         ,point(  -100f,   100f), rdc_meter)
         ,point(625000f, 10000f), rdc_meter)
         ,'spoint'
      ), point(0s,0s), point(3250s, 2700s)
   );

unit&lt;fpoint&gt; projFactor := <B>GetProjectionFactor(</B>rdc_100<B>)</B>;
</pre>

*result: projFactor = [(-100.0, 100.0)]*.

## see also

- [getprojectionbase](getprojectionbase)
- [getprojectionoffset](getprojectionoffset)