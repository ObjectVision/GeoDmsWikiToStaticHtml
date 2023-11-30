---
title: domainunit
layout: default
nav_exclude: true
---
*[unit-functions](unit-functions) DomainUnit*

## concept

1. [domain-unit](domain-unit) is a [unit](unit) with as role to define an entity.
2. DomainUnit() is a function to get the DomainUnit of an [attribute](attribute).

This page describes the DomainUnit() function.

## syntax

- DomainUnit(*a*)

## definition

DomainUnit(*a*) results in a unit with a reference to the **domain unit** of attribute *a*.

## example

<pre>
unit&lt;uint32&gt; RefADomain := <B>DomainUnit(</B>A<B>)</B>;
</pre>

## see also

- [valuesunit](valuesunit)
- [propvalue](propvalue)