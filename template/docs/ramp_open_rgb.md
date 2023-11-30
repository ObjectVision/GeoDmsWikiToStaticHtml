---
title: ramp_open_rgb
layout: default
nav_exclude: true
---
*[rescale-functions](rescale-functions) ramp_open_rgb*

## syntax

- ramp_open_rgb(*startvalue*, *uptovalue*, *domainunit*)

## definition

ramp_open_rgb(*startvalue*, *uptovalue*, *domainunit*) **ramps rgb values**, starting with the *startvalue* [argument](argument) up to the *uptovalue* argument.

The *uptovalue* argument itself is not part of the resulting [attribute](attribute).

The number of values is defined by the [cardinality](cardinality) of the [domain-unit](domain-unit) argument.

## applies to

- [parameter](parameter) *startvalue* and *uptovalue* with [value-type](value-type) uint32 (often configured with the [rgb](rgb) function)
- unit *domainunit* with value type from group CanBeDomainUnit

## since version

7.031

## example

<pre>
attribute&lt;uint32&gt; BrushColor (City) := <B>ramp_open_rgb(</B>rgb(255,255,0), rgb(0,255,0), City<B>)</B>;
</pre>

| **BrushColor**       |
|----------------------|
| **rgb(255, 255, 0)** |
| **rgb(218, 255, 0)** |
| **rgb(182, 255, 0)** |
| **rgb(145, 255, 0)** |
| **rgb(109, 255, 0)** |
| **rgb( 72, 255, 0)** |
| **rgb( 36, 255, 0)** |

*domain City, nr of rows = 7*

## see also

- [ramp_open](ramp_open)
- [ramp_rgb](ramp_rgb)