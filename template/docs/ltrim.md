---
title: ltrim
layout: default
nav_exclude: true
---
*[string-functions](string-functions) ltrim*

## syntax

- ltrim(*string_dataitem*)

## definition

ltrim(*string_dataitem*) **removes space characters** before the first non space character in *string_dataitem*.

## applies to

[data-item](data-item) *string_dataitem* with string [value-type](value-type)

## example

<pre>
attribute&lt;string&gt; ltrimA (ADomain) := <B>ltrim(</B>A<B>)</B>;
</pre>

| A                  | **ltrimA**            |
|--------------------|-----------------------|
| 'Test'             | **'Test**'            |
| '88hallo99'        | **'88hallo99**'       |
| '+)'               | **'+)**'              |
| 'twee woorden'     | **'twee woorden**'    |
| ' test met spatie' | **'test met spatie**' |

*ADomain, nr of rows = 5*

## see also

- [trim](trim)
- [rtrim](rtrim)