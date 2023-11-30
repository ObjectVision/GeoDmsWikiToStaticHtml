---
title: expression
layout: default
parent: how-to-model
nav_order: 22
---
The GeoDMS is intended to configure calculations, indicators, model components and chains. It offers a powerful set of [operators-and-functions](operators-and-functions) to configure and calculate the calculation/model logic in an efficient and transparent way. Quality control in the model logic is implemented by the management of dependencies and checking the consistency of calculations.

Although it is possible to execute external components with the GeoDMS, it is advised to configure especially the core components of a model in GeoDMS 
 operators & functions, to be able to use the full functionality of the GeoDMS modeling environment. External components keep their 'black box' character, which limit the transparency, efficiency and control of a the model configuration in the GeoDMS.

## characteristics
-   [management-of-dependencies](management-of-dependencies)
-   [constant-state-of-data-items](constant-state-of-data-items)
-   [explicit-configuration-of-value-types](explicit-configuration-of-value-types)
-   [subexpression](subexpression)
-   [unit-metric-consistency](unit-metric-consistency)

## how to configure
-   [expression-syntax](expression-syntax)
-   [indirect-expression](indirect-expression)
-   [external-components](external-components)

## fast calculations

The GeoDMS is used interactively, even with large data sets. This can only be achieved if calculations are performed fast, limiting the waiting time of the user for results.

Much attention in the development of the GeoDMS is being paid to efficient calculation processes. This is integral characteristic of the GeoDMS, taking into account the following aspects

-   [data-model](data-model)
-   [calculation-management](calculation-management)
-   [algorithmic-techniques](algorithmic-techniques)
-   [programming-architecture](programming-architecture)
-   [system-architecture](system-architecture)