---
title: geodms-default-tiling
layout: default
nav_exclude: true
---
# Default tiling
By default GeoDMS tiles data into segments of 256x256 blocks or 65536 rows.

# Tile pipelining
Most GeoDMS operators, even reading data using for instance gdal.grid, can make use of tile pipelines, which means that data can be processed on a per tile basis by multiple threads. Which in theory can reduce memory consumption significantly as there is no need to keep the full domain or compacted domain into memory. One property that can be set for instance when reading data pipelined is: LazyCalculated = "True".

# Optimal tiling of raster/grid SourceData
To optimally make use of GeoDMS internal default tiling data model, it is best to provide SourceData in 256x256 tiled blocks or in blocks of 65536 rows. The former 2D blocksize is more common for raster/grid datasets, for instance the [GeoTiff](https://gdal.org/drivers/raster/gtiff.html) format supports tiling. The tiling can be specified in most major GIS packages, for instance QGIS, which uses GDAL under the hood. It can also be specified using common gdal tools, for instance **gdalwarp**:

```
gdalwarp input.tif output.tif -co TILED=YES -co BLOCKXSIZE=256 -co BLOCKYSIZE=256 -s_srs ESRI:54009 -t_srs EPSG:4326 -co COMPRESS=LZW
```

# Using suboptimal tiling
Huge performance waste can be observed when using the GeoDMS default tiling and a dataset with tiling that diverts siginificantly from the default. For instance reading a GeoTiff for the whole world, with striped tiling of 1xN, with 1 row and N columns. This leads currently to the situation that in order to fill each internal tile of 256x256 pixels, 256 stripes need to be read. Which leads to reading (and possibly decompressing) the whole dataset multiple times. 