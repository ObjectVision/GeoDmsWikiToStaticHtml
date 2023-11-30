---
title: partioningname
layout: default
nav_exclude: true
---
*[allocation-functions](allocation-functions), argument 5: PartioningName*

## definition

*PartioningName* is the fifth [argument](argument) of the discrete_alloc function.

*PartioningName* is an [attribute](attribute) that maps each [partioningattribute](partioningattribute) to a [relation](relation) name.

The [domain-unit](domain-unit) of this attribute is the set of land use types.

## applies

-   attribute *PartioningName* with value type: string.

## example

<pre>
unit&lt;uint8&gt; lu_type: nrofrows = 3
{ 
   attribute&lt;string&gt; PartioningName: ['Living','Working','Nature'];
}
</pre>