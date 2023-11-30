---
title: export
layout: default
nav_exclude: true
---
With the GeoDMS data can be exported to multiple formats. This applies both to source data as well as calculated results.

Three types of exports are distinguished:
-   Export primary data to the clipboard
-   Export primary data to files
-   [export-viewports](export-viewports)

## clipboard

The table view can be used to export data to the clipboard with the following tools:

![](../assets/img/GUI/copy_text.png) copies the (selected) data from the table to the clipboard, string [data-item](data-item) are quoted and a semicolon is used as delimiter between the data item.

![](../assets/img/GUI/copy_picture.png) copies the visible contents of the active table as picture to the clipboard

More information on how to use the table view can be found in chapter 8 of the [user-guide](user-guide).

## primary data to files

Primary data can be exported to files in two ways:

1) By configuring a [storagemanager](storagemanager) to data items referring to calculation results, see topic: [data-source](data-source).

2) By using the [geodms-gui](geodms-gui) (see paragraph 15.3 of the User Guide). In the tree view a pop up menu option is available for each data item to
export primary data to the following formats:

-   Bitmap (*.TIF or *.BMP) (for data items with a [grid-domain](grid-domain))). The option exports data to (default and advised) [tif format](https://nl.wikipedia.org/wiki/Tagged_image_file_format) and optional [bmp](https://en.wikipedia.org/wiki/BMP_file_format) format.
-   Table (*.DBF with .shp and .shx where possible). This option exports data to [dbf format](https://en.wikipedia.org/wiki/DBase).
    If the data item refers to [vector-data](vector-data), the [geometry](geometry) is also exported to .shp/.shx format resulting in an
    [ShapeFile](https://nl.wikipedia.org/wiki/Shapefile).
-   [ascii-grid](ascii-grid) (for data items with a [grid-domain](grid-domain)). The option exports data to [Ascii
    grid](https://web.archive.org/web/20150128024528/http://docs.codehaus.org/display/GEOTOOLS/ArcInfo+ASCII+Grid+format)
    format.
-   [csv](csv) table for all data items. This option exports data to a [csv](https://en.wikipedia.org/wiki/Comma-separated_values) file with string fields quoted and a semicolon delimiter between all fields.