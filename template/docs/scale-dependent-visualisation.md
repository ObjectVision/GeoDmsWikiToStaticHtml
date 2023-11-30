---
title: scale-dependent-visualisation
layout: default
nav_exclude: true
---
Layers in the map view can be made [visualisation-style](visualisation-style) within a defined scale range. Detailed information can be shown if the user zooms in to a small area and more overview information if the user is zoomed out to a large area.

The MinPixSize and MaxPixSize [subitem](subitem) [parameter](parameter) for the [domain-unit](domain-unit) of the layer can be used for scale dependent visualisation.

## Example
<pre>
unit&lt;uint32&gt; house
:   StorageName = "%SourceDataDir%/house.csv"
,   StorageType = "gdal.vect"
{
   parameter&lt;float32&gt; ZoomInLimit  :=   0.00025f, DialogType = "<B>MinPixSize</B>";
   parameter&lt;float32&gt; ZoomOutLimit := 200.0f    , DialogType = "<B>MaxPixSize</B>";
}
</pre>

The ZoomInLimit parameter(The name of the subitem parameters have no functional meaning, but for transparency reasons it is advised to use clear names) with the [property](property) [dialogtype](dialogtype) configured to "MinPixSize", configures the lower limit of the zoom range for all data items with house as domain unit.The ZoomOutLimit with the property DialogType configured to "MaxPixSize" configures the upper limit.

The values for these limits are configured as [expression](expression) in the [metric](metric) of the coordinate system used, in the example meters. The configured parameters in the example define that this layer will be visualised if the zoom level is more than 0.00025 meter and less than 200.0 meter for one pixel.