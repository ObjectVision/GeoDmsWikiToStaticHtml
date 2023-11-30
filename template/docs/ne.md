---
title: ne
layout: default
nav_exclude: true
---
*[ordering-functions](ordering-functions) not equals (==)*

## syntax

-  ne(*a*, *b*)
-  *a* <> *b*

## definition

ne(*a*, *b*) or *a* <> *b* results in a boolean [data-item](data-item) indicating if the values of data item *a* are **not equal to** the corresponding values of data item *b*.

## description

The comparison between two missing values ([null](null) == null) results in the value False.

## applies to

Data items with Numeric, Point. string or bool [value-type](value-type)

## conditions

1.  [domain-unit](domain-unit) of the [argument](argument) must match or be [void](void) ([literals](https://en.wikipedia.org/wiki/Literal_(computer_programming)) or [parameter](parameter) can be compared to data items of any domain).
2.  [argument](argument) must have matching:
    - [value-type](value-type)
    - [metric](metric)

## example
<pre>
attribute&lt;bool&gt; AneB (CDomain) := <B>ne(</B>A, B<B>)</B>;
attribute&lt;bool&gt; AneB (CDomain) := A <B><></B> B;
</pre>

## see also

- [ne_or_one_null](ne_or_one_null)