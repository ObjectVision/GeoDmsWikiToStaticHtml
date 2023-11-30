---
title: invert
layout: default
nav_exclude: true
---
*[relational-functions](relational-functions) invert*

## syntax

- invert(*relation*)

## definition

invert(a) inverts the *[relation](relation)* [argument](argument).

Inverting means the resulting [attribute](attribute) has <B>as [domain-unit](domain-unit) the [values-unit](values-unit) and as values unit the domain unit</B> of the *relation* argument.

## applies to

- attribute *relation* with [value-type](value-type) of the group CanBeDomainUnit

## example

<pre>
attribute&lt;Region&gt; invertRegion_rel (Region) := <B>invert(</B>City/Region_rel<B>)</B>;
</pre>

| City/Region_rel |
|----------------:|
| 0               |
| 1               |
| 2               |
| 1               |
| 3               |
| null            |
| 3               |

*domain City, nr of rows = 7*

| **InvertRegion_rel** |
|---------------------:|
| **1**                |
| **4**                |
| **3**                |
| **7**                |
| **null**             |

*domain Region, nr of rows = 5*