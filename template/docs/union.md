---
title: union
layout: default
nav_exclude: true
---
*[relational-functions](relational-functions) union*

## syntax

- union(*a*, *b*)

## definition

union(*a*, *b*) results in a new uint32 [domain-unit](domain-unit) with all elements of the [attribute](attribute) *a* and *b*.

## description

The description for the union function is only available for backward compatibility purposes. The function has become obsolete in version 8.7.0. In new configurations, use the [union_unit](union_unit) and [union_data](union_data) functions instead.

## since version

5.15