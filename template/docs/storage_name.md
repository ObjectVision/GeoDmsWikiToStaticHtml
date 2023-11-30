---
title: storage_name
layout: default
nav_exclude: true
---
*[file,-folder-and-read-functions](file,-folder-and-read-functions) storage_name*

## syntax

- storage_name(*item_with_storage*)

## definition

storage_name(*item_with_storage*) results in a string [parameter](parameter) with the **value of the [storagename](storagename) [property](property)** configured for the *item_with_storage*.

[folders-and-placeholders](folders-and-placeholders) are expanded in the result.

## applies to

- [data-item](data-item) *item_with_storage* with a configured storage.

## example

<pre>
1. attribute&lt;uint8&gt;  griddata (GridUnit): StorageName = "%projdir%/data/testgrid.asc";
2. parameter&lt;string&gt; storage_name := <B>storage_name(</B>griddata<B>)</B>;
</pre>

*result: storage_name = 'c:/prj/tst/data/testgrid.asc'*

## see also

- [propvalue](propvalue)