---
title: propvalue
layout: default
nav_exclude: true
---
*[miscellaneous-functions](miscellaneous-functions) PropValue*

## syntax

- PropValue(*item*, *property*)

## definition

PropValue(*item*, *property*) results in a string [parameter](parameter) with the **value** of the ***[property](property)*** [argument](argument) for the *[tree-item](tree-item)* argument.

## applies to

*item* can be any tree item, not being itself or one of it's [subitem](subitem) (an invalid recursion error is generated)

There is a list of all [property](property).

## example

<pre>
attribute&lt;meter&gt; A (ADomain) := B + C,  descr = "A is the sum of B and C";
{
   parameter&lt;string&gt; name       := <B>PropValue(</B>A, 'name'<B>)</B>;       <I>result = 'A'</I>
   parameter&lt;string&gt; valuesunit := <B>PropValue(</B>A, 'ValuesUnit'<B>)</B>; <I>result = 'meter'</I>
   parameter&lt;string&gt; expr       := <B>PropValue(</B>A, 'expr'<B>)</B>;       <I>result = 'B + C'</I>
   parameter&lt;string&gt; descr      := <B>PropValue(</B>A, 'descr<B>)</B>;       <I>result = 'A is the sum of B and C'</I>
}
</pre>

## see also

- [subitem_propvalues](subitem_propvalues)
- [inherited_propvalues](inherited_propvalues)