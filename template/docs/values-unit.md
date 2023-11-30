---
title: values-unit
layout: default
nav_exclude: true
---
A values units describes how values of a data item need to be interpreted. A values unit consists of:

1.  a **value type** (required) which need to correspond to the type of data values configured with this values unit. The value type of the values unit defines the data type, dimension and allowed range of values, see the [value-type](value-type) table.
2.  a **[metric](metric)** (optional, advised for units describing quantities) defining how the values need to be interpreted semantically (in meters, seconds, etc.).

Values units describe [data-item](data-item) with a similar range of values. This makes these units suitable for the configuration of a [default-classification-scheme](default-classification-scheme) (cdf [property](property)).

## types

Values units can be split up into:

1.  **[base-unit](base-unit)** : units for which the [metric](metric) is explicitly configured with the [baseunit](baseunit) function,
2.  **[derived-unit](derived-unit)** : units configured with [expression](expression), combining other [unit](unit), [parameter](parameter) and [literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)). The metric results from the configured expression.
3.  **[value-type](value-type)**: value types can also be used als values unit. For [numerical](numerical) data, this is not advised as the metric of values units is useful in interpreting your data and in preventing illogical calculations.