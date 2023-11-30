---
title: uint32seq
layout: default
nav_exclude: true
---
*[sequence-functions](sequence-functions) uint32Seq*

## syntax

- uint32Seq(*a*)

## definition

uint32Seq(*a*) results in a **sequence of 32 bits unsigned integers** derived from string [data-item](data-item) *a*.

The syntax for string [argument](argument) *a* need to be: {10: 41 9999 42 10 600 1 7 116 0 110}.

In this string:
- The curly brackets {..} indicate the start and end of the sequence.
- The first number (10) indicates the number of elements of the sequence followed by a colon. The elements of the sequence follow this colon, separated by spaces.

The [composition](composition) need to be configured to poly. The [sequence2points](sequence2points) function can be used to make a pointset domain.

## applies to

- [data-item](data-item) *a* with a string [value-type](value-type)

## since version

7.130

## example
<pre>
parameter&lt;string&gt; param               := '{10: 41 9999 42 10 600 1 7 116 0 110}';
parameter&lt;uint32&gt; param_uint32 (poly) := <B>uint32Seq(</B>source/param<B>)</B>;
</pre>

| param_uint32                           |
|----------------------------------------|
| **{10: 41 9999 42 10 600 7 116 0 110}**|