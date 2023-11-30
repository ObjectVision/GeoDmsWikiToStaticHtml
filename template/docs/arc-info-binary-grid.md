---
title: arc-info-binary-grid
layout: default
nav_exclude: true
---
[Arc Info Binary Grid](https://en.wikipedia.org/wiki/Esri_grid) Files can be read with gdal.grid.

## example
<pre>
unit&lt;wpoint&gt; aig
: StorageName = "%sourcedatadir%/aigrid_test"
, StorageType = "gdal.grid"
, DialogData  = "Geography/WorldBaseUnit"
{
   unit&lt;wpoint&gt; World1kmGrid := TiledUnit(
         point(uint16(1024), uint16(1024), aig)
      );
   attribute&lt;uint8&gt; ReadData (World1kmGrid);
}
</pre>

The StorageName property refers to the folder with the grid data. The [projection](projection) information is also read from this folder.

The [dialogdata](dialogdata) property needs to refer to the base unit for the coordinate system to inform the GeoDMS on how to relate the
projection information from the grid file to the [how-to-configure-a-coordinate-system](how-to-configure-a-coordinate-system), in this case WorldBaseUnit.

The configured World1kmGrid is a [tiledunit](tiledunit). This unit is used to read the data from the binary grid file in [tile](tile) of 1024 * 1024 grid cells. 