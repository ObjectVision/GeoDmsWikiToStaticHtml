---
title: boundrange
layout: default
nav_exclude: true
---
*[unit-functions](unit-functions) boundrange*

## syntax

- boundrange(*unit*)

## definition

boundrange(*unit*) results in [parameter](parameter) with the **size of the range** of the *unit* [argument](argument).

The [values-unit](values-unit) of the resulting parameter is the *[unit](unit)* argument

## applies to

- unit *unit* with Numeric or Point value type

## example

<pre>
unit&lt;float32&gt;      domainB: nrofrows = 6;
parameter&lt;domainB&gt; boundrange_domainB := <B>boundrange(</B>domainB<B>)</B>;
</pre>

*result boundrange_domainB = 6*

## see also

- [upperbound](upperbound)
- [lowerbound](lowerbound)
- [boundcenter](boundcenter)