---
title: network-functions
layout: default
parent: operator
nav_order: 43
---
Network [operators-and-functions](operators-and-functions) are used to build and calculate with [network topologies](https://en.wikipedia.org/wiki/Network_topology) like [connect](connect) or [impedance-functions](impedance-functions)

- [first_node](first_node) - *a point data item with the coordinates of the first point of an arc or polygon*
- [last_node](last_node)  - *a point data item with the coordinates of the last point of an arc or polygon*

<!-- -->

- [connect](connect) - *creates the nearest point on an arc/polygon data item from a point data item or finds the nearest point in a point data item from another point data item*
- [connect_eq](connect_eq) - *creates the nearest point on an arc/polygon data item from a point data item if the values of two data items match*
- [connect_ne](connect_ne) - *creates the nearest point on an arc/polygon data item from a point data item if the values of two data items do not match*
- [connect_neighbour](connect_neighbour) - *a relation to the nearest point in the same point data item, not being the point itself*
- [connect_info](connect_info) - *information for each point on the connection to an arc/polygon data item, as made by the connect function*
- [connect_info_eq](connect_info_eq) - *information for each point on the connection to an arc/polygon data item, as made by the connect_eq function*
- [connect_info_ne](connect_info_ne) - *information for each point on the connection to an arc/polygon data item, as made by the connect_ne function*
- [connected_parts](connected_parts) - *the connected (sub)networks that exist in a set of links*
- [capacitated_connect](capacitated_connect) - *finds the nearest point in a point data item from another point data item with a capacity constraint*

<!-- -->

- [impedance-general-(formerly-known-as-dijkstra)](impedance-general-(formerly-known-as-dijkstra)) - *a description of the dijkstra algorithm*
- [impedance-key-entities](impedance-key-entities) - *a description on nodes and links*
- [impedance-functions](impedance-functions) - *how to apply the impedance function*
- [impedance-options](impedance-options) - *optional parameters of the impedance function*
- [impedance-warning](impedance-warning) - *warning if the impedance is applied with very large datasets*
- [impedance-interaction-potential](impedance-interaction-potential) - *additional information on the concept of interaction potential*
- [impedance-additional](impedance-additional) -*some additional information on impedance functions*
- [impedance-future](impedance-future) - *our ideas on potential future impedance functionality*
- [impedance-links](impedance-links) - *interesting links*
- [impedance-example-origin-to-nearest-destination](impedance-example-origin-to-nearest-destination) - *an example of how to apply the impedance function to calculate the distances of a point set to the nearest point in another point set*

<!-- -->

- [impedance-obsolete-dijkstra](impedance-obsolete-dijkstra)
- [impedance-obsolete-dijkstra-od](impedance-obsolete-dijkstra-od)
- [impedance-obsolete-dijkstra-directed](impedance-obsolete-dijkstra-directed)

<!-- -->

- [trace_back](trace_back) - *the amount of flow for each link in the network.*
- [service_area](service_area) - *the relation to the nearest destination node for each node in the node set.*