---
title: asdatastring
layout: default
nav_exclude: true
---
*[string-functions](string-functions) AsDataString*

## syntax

- AsDataString(*string_dataitem*)

## definition

- AsDataString(*string_dataitem*) results in a string [parameter](parameter) with **all values** of *string_dataitem*, **comma delimited** and **single quoted**.

## applies to

- [data-item](data-item) *string_dataitem* with string [value-type](value-type)

## example

<pre>
parameter&lt;string&gt; CityListParam := <B>AsDataString(</B>City/Name<B>)</B>;  
<I> result = 'Groningen,Delfzijl,Winschoten,Leeuwarden,Dokkum,Bolsward,Emmen,Assen,Hoogeveen'</I>
</pre>

| City/Name    | 
|--------------|
| 'Groningen'  |
| 'Delfzijl'   |
| 'Winschoten' |
| 'Leeuwarden' |
| 'Dokkum'     |
| 'Bolsward'   |
| 'Emmen'      |
| 'Assen'      |
| 'Hoogeveen'  |

*domain City, nr of rows = 9*

## see also

- [aslist](aslist)
- [asexprlist](asexprlist)
- [asitemlist](asitemlist)