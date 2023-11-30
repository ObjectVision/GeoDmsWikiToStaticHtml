---
title: valuesunit
layout: default
nav_exclude: true
---
*[unit-functions](unit-functions) ValuesUnit*

## concept

1. [values-unit](values-unit) is a [unit](unit) with as role to define the [value-type](value-type) and [metric](metric) of the values of a [data-item](data-item).
2.  ValuesUnit() is a function to get the Values Unit of an [attribute](attribute).

This page describes the ValuesUnit() function.

## syntax

- ValuesUnit(*a*)

## definition

ValuesUnit(*a*) results in a unit with a reference to the **[values-unit](values-unit)** of attribute *a*.

## example
<pre>
unit&lt;uint32&gt; RefADomain := <B>ValuesUnit(</B>A<B>)</B>;
</pre>

## see also

- [domainunit](domainunit)
- [propvalue](propvalue)