---
title: tree-item
layout: default
nav_exclude: true
---
## definition

All elements that occur in a configuration are called tree items. Four types of tree items are distinguished:

- [unit](unit)
- [data-item](data-item)
- [container](container)
- [template](template)

## name

Each tree item is configured with a keyword (unit, attribute, parameter, container or template) and at least a [tree-item-name](tree-item-name).

## full name

Based on the hierarchical structure, a full name can be derived for each tree item. This full name includes the name of the item and the name of all it's parents.

This full name is comparable to a full file path in a directory structure.

## properties

Properties can be configured as relevant characteristics for an item. To configure a property use:

- A [colon (:)](https://en.wikipedia.org/wiki/Colon_(punctuation)) after the name of the item, before the first property.
- [Commas (,)](https://en.wikipedia.org/wiki/Comma) as separators between properties

## example

<pre>
attribute&lt;meter&gt; length (road) := arc_length(geometry), descr = "length of the road";
</pre>

In the example an [attribute](attribute) tree item is configured with as:

1.  [values-unit](values-unit): meter
2.  [tree-item-name](tree-item-name): length
3.  [domain-unit](domain-unit): road
4.  two [property](property), an expression: _arc_length(geometry)_ and a description: length of the road.