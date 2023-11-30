---
title: typenames
layout: default
nav_exclude: true
---
*[allocation-functions](allocation-functions), argument 1: TypeNames*

## definition

*TypeNames* is the first [argument](argument) of the discrete_alloc function.

*TypeNames* is an attribute with the name of each land use type.

The [domain-unit](domain-unit) of this attribute is the set of land use types.

## applies to

attribute TypeNames with [value-type](value-type): string

## conditions

The names of the land use types need to match with the name of the [subitem](subitem) of the following arguments of the discrete_alloc function:

-   *[suitabilitymaps](suitabilitymaps)*
-   *[minclaims](minclaims)*
-   *[maxclaims](maxclaims)*

## example

<pre>
unit&lt;uint8&gt;> lu_type: nrofrows = 3
{
   attribute&lt;string&gt; Name: ['Living','Working','Nature'];`
}
</pre>