---
title: operators-and-functions
layout: default
nav_exclude: true
---
[Operators](https://en.wikipedia.org/wiki/Operator_(mathematics)) and [functions](https://en.wikipedia.org/wiki/Function_(mathematics)) are
used in expressions to calculate with [data-item](data-item) and or [literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)).

## operators

An [operator](operator) is a symbolic presentation of a function to be applied on [operands](https://en.wikipedia.org/wiki/Operand).

## functions

Functions express dependences between items. A function associates a single output to each input element. Functions in the GeoDMS are categorized in the following function groups:

-   **[arithmetic-functions](arithmetic-functions)**: basic [mathematical functions](https://en.wikipedia.org/wiki/Mathematics), like [add](add), [div](div) or
[sqrt](sqrt)
-   **[ordering-functions](ordering-functions)**: to compare/order data items like [eq](eq), [lt](lt), [argmax](argmax) or [sort](sort)
-   **[aggregation-functions](aggregation-functions)**: to aggregate data items to other domain units like [sum](sum) or [mean](mean)
-   **[conversion-functions](conversion-functions)**: to convert [value-type](value-type), round data items or use different notations
-   **[classify-functions](classify-functions)**: to classify [quantities](https://en.wikipedia.org/wiki/Quantity) to class units 
-   **[transcendental-functions](transcendental-functions)**: functions [transcending algebra](https://en.wikipedia.org/wiki/Transcendental_function),
    like [exponent](exponent) and [logarithm](logarithm)
-   **[predicates-functions](predicates-functions)**: to check conditions, like [isdefined](isdefined) of [isnull](isnull).
-   **[logical-functions](logical-functions)**: to provide basic comparisons, returning in boolean data items like [iif](iif) or [and](and)
-   **[relational-functions](relational-functions)**: to relate data items of different domain units like [lookup](lookup) or create new domain units like [unique](unique)
-   **[selection-functions](selection-functions)**: to create new domain units for selections of data from other domain units like [select_with_attr_by_cond](select_with_attr_by_cond)
-   **[rescale-functions](rescale-functions)**: to scale data items to new distributions
-   **[constant-functions](constant-functions)**: to define constant values like [pi](pi) or [true](true)
-   **[trigonometric-functions](trigonometric-functions)**: operate on angles like [sin](sin) or [cos](cos).
-   **[geometric-functions](geometric-functions)**: geometric operations on [point](point), [arc](arc) and/or [polygon](polygon)
-   **[network-functions](network-functions)**: to build and calculate [network topologies](https://en.wikipedia.org/wiki/Network_topology) like [connect](connect) or     [impedance-functions](impedance-functions)
-   **[grid-functions](grid-functions)**: to calculate with data items of [grid-domain](grid-domain), like [potential](potential) or [district](district)
-   **[string-functions](string-functions)**: operate on data items with string value types like [left](left) or [strcount](strcount)
-   **[file,-folder-and-read-functions](file,-folder-and-read-functions)**: operate on files and folders, like [makedir](makedir) or [storage_name](storage_name)
-   **[unit-functions](unit-functions)**: to define and get information of [unit](unit) items, like [range](range)and [lowerbound](lowerbound)
-   **[matrix-functions](matrix-functions)**: to perform [matrix](https://en.wikipedia.org/wiki/Matrix_(mathematics)) calculations, like 
[matrix-multiplication](matrix-multiplication) or [matrix-inverse](matrix-inverse)
-   **[sequence-functions](sequence-functions)**: process data items with one-dimensional [sequences](https://en.wikipedia.org/wiki/Sequence).
-   **[metascript-functions](metascript-functions)**:to generate script (like [for_each](for_each)) or request information on [tree-item](tree-item) like [subitem_propvalues](subitem_propvalues)
-   **[allocation-functions](allocation-functions)**: mainly used for [Land Use Allocation](https://github.com/ObjectVision/LandUseModelling/wiki/Allocation)
-   **[miscellaneous-functions](miscellaneous-functions)**: remaining functions not categorized in other groups, like [rnd_uniform](rnd_uniform) or [propvalue](propvalue)