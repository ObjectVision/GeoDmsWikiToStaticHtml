---
title: parameter
layout: default
nav_exclude: true
---
Parameters are [data-item](data-item) referring to one value. No [domain-unit](domain-unit) needs to be configured.

## syntax

- Start with the keyword: **parameter**
- Configure between the less than (\<) and greater than (>) characters, it's [values-unit](values-unit).
- Next configure the name of the parameter.
- The parameter value is often configured as [expression](expression) (see first example) but also other [property](property) can be configured (see second
example).
- To finalize the definition of an item, configure a [semicolon (;)](https://en.wikipedia.org/wiki/Semicolon) character.

## example
<pre>
parameter&lt;periods&gt; nrPeriods  := 4;
parameter&lt;string&gt;  RegionName := "Europe";
</pre>