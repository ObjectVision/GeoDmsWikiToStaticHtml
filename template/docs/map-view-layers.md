---
title: map-view-layers
layout: default
nav_exclude: true
---
_[user-guide-geodms-gui](user-guide-geodms-gui)_ - [map-view](map-view) layers

## layers
A map view consists of one or multiple layers, with coordinates expressed in the same coordinate system.

In the GeoDMS a distinction can be made in the following layer types:

## geodms data layers

Layers use to present data related to a [geographic-grid-domain](geographic-grid-domain). Such a domain can be visualised in a map view with [grid](grid) (for [grid-domain](grid-domain)), [polygon](polygon), [arc](arc) or [point](point)  (for [one-dimensional-domain](one-dimensional-domain)) as in the following example:

![](../assets/img/GUI/layer_types.png)<br>
_examples of data layers with grid, polygons, arcs and points data_

In these layers, the grid cell, polygons, arcs and/or points are visualized with one or multiple [visualisation-style](visualisation-style) (colors, symbols, size etc.). The possible styles are dependent on the layer type.

The following data layers can be distinguished:

### geographic layers
[feature-attribute](feature-attribute) of [one-dimensional-domain](one-dimensional-domain) can be directly drawn in a mapview, with a default or preconfigured [visualisation-style](visualisation-style).  

### thematic layers 
Thematic layers present a theme, usually a numeric data item, in a map. For [numeric-data-type](numeric-data-type) data, an distinction need to be made in [numerical](numerical) and [categorical](categorical) data. Categorical data can often be directly visualised, with a [visualisation-style](visualisation-style) for each category/class (default or preconfigured). Numerical data need to be classified first in a limited set of classes. Such a classification, and it's visualisation styles, can also be a a preconfigured or a default [default-classification-scheme](default-classification-scheme). 

More information on how to configure a classification scheme van be found in the [classification](classification) section. 

The GUI also contains a [classification-and-palette-editor](classification-and-palette-editor) to edit class breaks and color visualisation styles.

### label layers
[string](string) data items, with as feature type [point](point) or [polygon](polygon), are by default visualised as **label layer**, see example 

![](../assets/img/GUI/layer_label.png)<br>
_examples of label data layers for polygon and point data_

Also numeric values for these feature types can visualized as label layer, from the legend menu on the numeric layer, option Select Sublayer > Label > Visible. 

For [arc](arc) and [grid](grid) layers, label layers are not (yet) implemented. String data items of an arc layer are presented as geographic layer. 

## background layers

A [background-layer](background-layer) is visualized automatically when a view for the coordinate system for which this layer is configured is created. The background layer is used as a reference and is usually a WMTS layer. 

## active layer

![](../assets/img/GUI/layer_active.png)<br>

Each map view has one active layer, shown in the title of the map view. The active layer is the layer on which the layer-specific (toolbar) functions are executed. A layer can be activated from the legend. In this legend the active layer is indicated by a blue background color in the title as in the figure.

The user can switch between active layers by clicking on the layer title. By default, the last layer added to the map view becomes the active layer.