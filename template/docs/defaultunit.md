---
title: defaultunit
layout: default
nav_exclude: true
---
*[unit-functions](unit-functions) DefaultUnit*

## syntax

- DefaultUnit(*valuetype*)

## definition

DefaultUnit(valuetype) results in a unit with as [value-type](value-type) the **[literal](https://en.wikipedia.org/wiki/Literal_(computer_programming)) *valuetype***

## example

<pre>
unit&lt;string&gt; unit_str := <B>DefaultUnit(</B>'string'<B>)</B>;
</pre>