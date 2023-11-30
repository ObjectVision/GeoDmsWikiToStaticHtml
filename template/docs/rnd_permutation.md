---
title: rnd_permutation
layout: default
nav_exclude: true
---
*[miscellaneous-functions](miscellaneous-functions) rnd_permutation*

## syntax

- rnd_permutation(*seed*, *domainunit*)

## definition

rnd_permutation(*seed*, *domainunit*) results in a **random [permutation](https://en.wikipedia.org/wiki/Permutation)** of the [index-numbers](index-numbers) of the *domainunit* [argument](argument) with the following arguments:

- a *seed* with a unique number; using the same *seed* results in the same random order;
- unit *domainunit*, the [domain-unit](domain-unit) for which the permutation is made;

## applies to

- [data-item](data-item) *seed* with uint32 [value-type](value-type)
- [unit](unit) *domainunit* with valuetype from the group CanBeDomainUnit

## since version

5.68

## example

<pre>
attribute&lt;ADomain&gt; rand_order (ADomain) := <B>rnd_permutation(</B>0, ADomain<B>)</B>;
</pre>

| **rand_order** |
|---------------:|
| **1**          |
| **0**          |
| **3**          |
| **4**          |
| **2**          |

*ADomain, nr of rows = 5*

## see also

- [rnd_uniform](rnd_uniform)