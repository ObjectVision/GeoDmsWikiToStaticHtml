---
title: ramp
layout: default
nav_exclude: true
---
*[rescale-functions](rescale-functions) ramp*

## syntax

- ramp(*startvalue*, *endvalue*, *domain unit*)

## definition

ramp(*startvalue*, *endvalue*, *domainunit*) **ramps values**, starting with the *startvalue* [argument](argument) and ending with the *endvalue* argument.

The number of values is defined by the [cardinality](cardinality) of the *[domain-unit](domain-unit)* argument.

## applies to

unit *domain unit* with [value-type](value-type) from group CanBeDomainUnit

## since version

7.031

## example

<pre>
attribute&lt;uint32&gt; ramped (City) := <B>ramp(</B>0, 70, City<B>)</B>;
</pre>

| **ramped** |
|-----------:|
| **0**      |
| **11**     |
| **23**     |
| **35**     |
| **46**     |
| **58**     |
| **70**     |

*domain City, nr of rows = 7*

## see also

- [ramp_open](ramp_open)