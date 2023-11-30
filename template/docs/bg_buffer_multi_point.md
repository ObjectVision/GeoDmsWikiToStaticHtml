---
title: bg_buffer_multi_point
layout: default
nav_exclude: true
---
*[geometric-functions](geometric-functions) bg_buffer_multi_point*

![](../assets/img/GUI/bg_buffer_multi_point.png)

## syntax

- bg_buffer_multi_point(*arc/polygon_data_item*, *size*, *nr_angles*)

## definition

bg_buffer_multi_point(*arc/polygon_data_item*, *size*, *nr_angles*) results in a multi [polygon](polygon) [data-item](data-item) with <B>buffer circles around each coordinate</B> in the *arc/polygon_data_item*. The resulting data item has the same [domain-unit](domain-unit) as the *arc/polygon_data_item*.

The *size* arguments indicates the buffer circle size.

The *nr_angles* arguments indicates how many angles are used to make the buffer circles. More angles results in smoother circles but also in more data.

The *bg_* prefix of the function name indicates that the implementation of operator uses [boost geometry](https://www.boost.org/doc/libs/1_80_0/libs/geometry/doc/html/index.html)
library, more specifically, the [buffer](https://www.boost.org/doc/libs/1_80_0/libs/geometry/doc/html/geometry/reference/algorithms/buffer/buffer_4.html)
function.

## applies to

- [attribute](attribute) *arc/polygon_data_item* with a point [value-type](value-type) and [[composition](composition) arc or polygon
- [parameter](parameter) *size* with a [float64](float64) value type
- parameter *nr_angles* with a [uint8](uint8) value type

## since version

7.413

## example

<pre>
attribute&lt;fpoint&gt; buffer_circles (polygon, district) := <B>bg_buffer_multi_point(</B>district/geometry, 10.0, 16b<B>)</B>;
</pre>

more examples of buffer functions can be found here: [buffer-processing-example](buffer-processing-example)

## see also

- [bg_buffer_point](bg_buffer_point)
- [bg_buffer_linestring](bg_buffer_linestring)
- [bg_buffer_multi_polygon](bg_buffer_multi_polygon)