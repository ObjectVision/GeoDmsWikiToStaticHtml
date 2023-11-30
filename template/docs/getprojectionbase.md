---
title: getprojectionbase
layout: default
nav_exclude: true
---
*[unit-functions](unit-functions) GetProjectionBase*

## syntax

- *GetProjectionBase(*gridunit*)*

## definition

GetProjectionBase(*gridunit*) results in a reference for the *gridunit* towards the **[unit](unit) used for the [grid-domain](grid-domain)** (e.g. meters for RD and degrees for LatLong).

## applies to

- unit *gridunit* with Point [value-type](value-type) of the group CanBeDomainUnit

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

unit&lt;fpoint&gt; projBase := <B>GetProjectionBase(</B>rdc_100<B>)</B>;
</pre>

*result: The projBase unit will refer to the rdc_meter unit*.

## see also

- [getprojectionoffset](getprojectionoffset)
- [getprojectionfactor](getprojectionfactor)