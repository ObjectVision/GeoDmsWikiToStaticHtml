---
title: expand
layout: default
nav_exclude: true
---
*[string-functions](string-functions) expand*

## syntax

- expand(*item*, *placeholderString*)

## definition

expand(*item*, *placeholderString*) results in a string [parameter](parameter) with the **expanded value** of the *placeholderString* in the context of the *item* [argument](argument).

## description

Expansion means placeholders are replaced by (sub)folders on the local machine. See [folders-and-placeholders](folders-and-placeholders) for more information on placeholders.

## applies to

- [tree-item](tree-item)
- string [parameter](parameter) *placeholderString*

## since version

5.60

## example

<pre>
parameter&lt;string&gt; LocalDataProjDir := <B>expand(</B>. ,'%localDataProjDir%'<B>)</B>;
</pre>

*result: LocalDataDir = 'C:/LocalData/operator' (or based on the value of another %localDataProjDir% configured)*