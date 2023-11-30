---
title: getmetricfactor
layout: default
nav_exclude: true
---
*[unit-functions](unit-functions) GetMetricFactor*

## syntax

- GetMetricFactor(*values unit*)

## definition

GetMetricFactor(*values unit*) results in a float64 [data-item](data-item) with the **factor in the [metric](metric)** of the *[values-unit](values-unit)* [argument](argument).

## applies to

- argument *values unit* with Numeric or Point [value-type](value-type)

## since version

5.44

## example
<pre>
unit&lt;float32&gt;      ha           := 10000.0 * m * m;
unit&lt;float32&gt;      per_ha       := 1.0 / ha;
parameter&lt;float64&gt; MetricFactor := <B>GetMetricFactor(</B>per_ha<B>)</B>;
</pre>

*result: MetricFactor = 0.0001*

## see also

- [propvalue](propvalue)