---
title: strlen
layout: default
nav_exclude: true
---
*[string-functions](string-functions) strlen(gth)*

## syntax

- strlen(*string_dataitem*)

## definition

strlen(*string_dataitem*) results in an uint32 [data-item](data-item) with the **length of each string value** of [argument](argument) *string_dataitem*.

## applies to

[data-item](data-item) *string_dataitem* with string [value-type](value-type)

## example

<pre>
attribute&lt;uint32&gt; strlenA (ADomain) := <B>strlen(</B>A<B>)</B>;
</pre>

| A                  |**strlenA** |
|--------------------|-----------:|
| 'Test'             |   **4**    |
| '88hallo99'        |   **9**    |
| '+)'               |   **2**    |
| 'twee woorden'     |   **12**   |
| ' test met spatie' |   **16**   |

*ADomain, nr of rows = 5*

## see also

- [strlen64](strlen64)