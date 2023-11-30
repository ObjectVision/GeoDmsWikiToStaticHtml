---
title: map-view
layout: default
nav_exclude: true
---
_[user-guide-geodms-gui](user-guide-geodms-gui)_ - map view

## introduction

The map view presents [data-item](data-item) that can be geographically located. Each map view has a [projection](https://en.wikipedia.org/wiki/Map_projection), indicating a coordinate system. For instance in Dutch applications usually the "[Rijks Driehoek (RD)](https://nl.wikipedia.org/wiki/Rijksdriehoeksco%C3%B6rdinaten)" coordinate system is used. [EPSG](https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset) codes are used as identifiers for the most common coordinate systems. The EPSG code is shown in the title of each map view, if configured as [spatialreference](spatialreference) [property](property) for the base unit of the [how-to-configure-a-coordinate-system](how-to-configure-a-coordinate-system).

A map view consists of layers, each layer is related to one or more data items. All geographically related data items using the same projection can be combined in the same map view window. They can also be opened in multiple separate map views. The number of opened map views is not limited.

By double clicking on an element, a [valueinfo](valueinfo) window appears.

## activate map view  

To view data in a map view, first activate a [tree-item](tree-item) that can be geographically related (indicated with a map icon ![](../assets/img/GUI/tv_globe.bmp)). 

A new map can be created or a layer can be added to an existing map by activating one of the following actions listed in the table. 

|action|no active map view|active map view|
|------|------------------|----------------|
|**double click** on active item|new map window|added to active map view with same coordinate system|
|main/pop-up menu option **default view**|new map window|added to active map view with same coordinate system|
|main/pop-up menu option **map view**|new map window|new map window| 
|**Ctrl-M** on active item|new map window|new map window| 
|**drag and drop** to view|new map window|added to active map view with same coordinate system| 

## topics
- [map-view-layers](map-view-layers)
- [map-view-tools](map-view-tools)
- [map-view-legend](map-view-legend)

