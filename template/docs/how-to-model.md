---
title: how-to-model
layout: default
has_children: true
nav_order: 18
---
Modelling in GeoDMS terms is the process of writing/editing a (set of) configuration file(s). 
In these files usually [data-source](data-source) is read and [expression](expression) are configured.

The [geodms-gui](geodms-gui) can be used as a tool in developing your model.

It is a good habit to also document your configuration.

## project

A GeoDMS project usually consists of:
-   (a set of) configuration files
-   source data
-   documentation

## configuration files

The GeoDMS uses a configuration language to configure source data, calculation steps, visualisation styles, export settings and relevant descriptive information. This information is stored in [configuration-file](configuration-file).

## declarative language

The GeoDMS configuration language is a [declarative](https://en.wikipedia.org/wiki/Declarative_programming) language. This means you configure what needs to be calculated and how the results needs to be presented. How calculations are performed in an efficient way is encapsulated in the implementation of each [operators-and-functions](operators-and-functions) that can be configured in an [expression](expression).

## topics
-   [configuration-basics](configuration-basics)
-   [unit](unit)
-   [data-source](data-source)
-   [numeric-data-type](numeric-data-type)
-   [expression](expression)
-   [geography](geography)
-   [relational-model-versus-semantic-arrays](relational-model-versus-semantic-arrays)
-   [template](template)
-   [classification](classification)
-   [visualisation-style](visualisation-style)
-   [export](export)
-   [naming-conventions](naming-conventions)
-   [value-type](value-type)
-   [folders-and-placeholders](folders-and-placeholders)
-   [property](property)