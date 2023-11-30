---
title: impedance
layout: default
nav_exclude: true
---
The impedance is a resistance measure for travelling a network and/or it's parts. The impedance can e.g. indicate:
- the distance of the link(s) (the [arc_length](arc_length) function can be used to calculate the length af an [arc](arc));
- the travel time;
- the travel costs.

In Dutch the word reisweerstand is used for impedance.

## GeoDMS implementation

The impedance is implemented as a [data-item](data-item) with a set of links as [domain-unit](domain-unit) and a (additive, non-negative) resistance measure as its 
[values-unit](values-unit), like meter or second.

## functions

Impedances are [argument](argument) of the [impedance-obsolete-dijkstra](impedance-obsolete-dijkstra).