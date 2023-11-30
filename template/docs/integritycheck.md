---
title: integritycheck
layout: default
nav_exclude: true
---
In modelling, especially when complexity rises, errors are easily made.

The GeoDMS contains ways of assisting modeller's on tracking down and solving errors, think for instance on [unit-metric-consistency](unit-metric-consistency).

Another useful feature is the configuration of integrity checks for [data-item](data-item).

An IntegrityCheck is used to check if an (intermediate) result meets certain requirements, for instance that all values need to be within a certain range or that no missing data may occur.

if an IntegrityCheck fails, the data of the resulting items can usually still be requested in a table view, in order to find out what is wrong. The data can not be exported.

If you write an expression in the IntegrityCheck, you can use 'this' to refer to itself. This is preferred. 

```
container ReadOpbrengsten_perOP  := 
	for_each_neidv(OP/name
		, 'ReadOpbrengsten_perOP_UNCHECKED/'+OP/name
		, '(all(IsNull(this)))'
		, AdminDomain
		, EUR
	);
```


## examples

### No missing data

<pre>
attribute&lt;city&gt; city_rel (neighborhood) := rlookup(city_code, regions/city/city_code)
, <B>IntegrityCheck</B> = "isDefined(city_rel)";
</pre>

The [attribute](attribute) uses the [rlookup](rlookup) function to find the [relation](relation) to the regions/city [domain-unit](domain-unit).<BR> 
The configured IntegrityCheck checks if for each neighborhood a city is found.

In such an IntegrityCheck it is allowed to refer to the item for which the IntegrityCheck is configured, the GeoDMS has a workaround to work with such self references.

### Recent version

<pre>
container root: IntegrityCheck = "GeoDmsVersion() >= 7.123"
</pre>

This IntegrityCheck at the root container of the configuration checks if the configuration is opened in a GeoDMS version 7.123 or later.

### see also
- an integrity check can also be used in a [for_each](for_each) loop.