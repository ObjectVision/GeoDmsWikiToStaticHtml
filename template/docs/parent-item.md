---
title: parent-item
layout: default
nav_exclude: true
---
The GeoDMS uses a hierachical structure for [tree-item-name](tree-item-name) [tree-item](tree-item) in a configuration.

The parent item of an item A is the item one level higher, of which item A is a [subitem](subitem). The parent items of the parent item of A are the indirect parent items of A.

The root item in a configuration has no parent item.

a point (.) in the configuration refers to the direct parent item, two points (..) to the parent of the parent etc.  