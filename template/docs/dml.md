---
title: dml
layout: default
nav_exclude: true
---
*[relational-model-versus-semantic-arrays](relational-model-versus-semantic-arrays) DML*

In the relational model a [DML (data manipulation language)](https://en.wikipedia.org/wiki/Data_manipulation_language) is used to select, insert, update or delete data in a database. [SQL](https://en.wikipedia.org/wiki/SQL) is one of the most used [DML](https://en.wikipedia.org/wiki/Data_manipulation_language) (as well as [DDL](https://en.wikipedia.org/wiki/Data_definition_language)) language.

The GeoDMS modelling language is a [functional programming language](https://en.wikipedia.org/wiki/Functional_programming).
Programming is done with [expression](expression) instead of statements, avoiding changing-state and mutable data. The GeoDMS is also not meant to manage data in external databases. Therefore there are no GeoDMS functions for SQL Insert, Update, Delete and Select Into Statements.

## SQL Select

The SQL Select is used to make selections of data from one or more tables/views in a desired sequence. The SQL statement implicitly creates a new view, which can be used as a table, with a selection of the records of the original table(s)/view(s).

As the GeoDMS works with semantic arrays, new [domain-unit](domain-unit) need to be configured before the [data-item](data-item) can be configured. The GeoDMS has a set of [relational-functions](relational-functions). These functions often result in mappings towards the original domain units, which can be used to define the new data items.

## examples

-   [select-...-from-...](select-...-from-...)
-   [select-...-from-...-where-...](select-...-from-...-where-...)
-   [select-...-from-...-order-by...](select-...-from-...-order-by...)
-   [select-...-from-...-where-...-order-by...](select-...-from-...-where-...-order-by...)
-   [distinct](distinct)
-   [select-...-from-...-group-by-...](select-...-from-...-group-by-...)
-   [select-...-from-...-inner-join-....-on-...](select-...-from-...-inner-join-....-on-...)
-   [select-...-from-...-left_right-join-...-on-...](select-...-from-...-left_right-join-...-on-...)
-   [select-...-from-...-...](select-...-from-...-...) 