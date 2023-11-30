---
title: valueinfo
layout: default
nav_exclude: true
---
_[user-guide-geodms-gui](user-guide-geodms-gui)_ - value info

## tracing the calculation path

![](../assets/img/GUI/valueinfo.png)<br>

The value info dialog presents the trace on how individual cells in a [table-view](table-view) or elements in a [map-view](map-view) are calculated.
 
The example shows the value info dialog for a cell in the table, presenting [parameter](parameter) _c_ with as value: 12.
This value is calculated by multiplying two other parameters, _A_ with a value of 3 and _B_ with a value of 4.
The value info dialog presents these parameters and their values. For [attribute](attribute) it would also present the relevant values needed to calculate the requested value.

If for instance the value 4 of parameter _B_ is also the result of a calculation, click on the value 4 to get the value info for this value. Step by step, you can trace the whole calculation path, until the final sources (data read from source files) are reached. Backward and Forward buttons are available, to assist the user in tracing backward and forward in the calculation path.      