---
title: relation
layout: default
nav_exclude: true
---
A relation or relational attribute is an [attribute](attribute) containing as values the [ordinal number](https://en.wikipedia.org/wiki/Ordinal_number) of the elements of another domain. It thereby defines a mapping from each element of the domain for which it is an attribute to that other [domain-unit](domain-unit). The following picture illustrates this:

![](../assets/img/GUI/relation_small.gif)

A relation has the source domain as domain unit and the related/target domain as [values-unit](values-unit). It's a mapping from the source towards the elated/target domain.

Synonyms in use for relation: [partitioning](partitioning), [index-attribute](index-attribute), relational attribute;

## naming convention

It is advised to use the postfix _rel when naming index attributes, see also [naming-conventions](naming-conventions).

## how to make

Relations are often made with a [rlookup](rlookup) or [point_in_polygon](point_in_polygon) function. See also [relational-attribute-example](relational-attribute-example).

## use

Relations are often used in [relational-functions](relational-functions) and [aggregation-functions](aggregation-functions).