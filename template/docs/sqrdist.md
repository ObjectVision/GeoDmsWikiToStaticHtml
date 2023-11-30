---
title: sqrdist
layout: default
nav_exclude: true
---
*[geometric-functions](geometric-functions) sq(ua)r(e)dist(ance)*

## syntax

- sqrdist(*destination*, *origin*)

## definition

sqrdist(*destination*, *origin*) calculates the <B>square distance (as the crow flies) between *origin* and *destination* [point](point)</B> of the same [domain-unit](domain-unit).

The resulting [data-item](data-item) has a float32 [value-type](value-type) without [metric](metric). Use the [value](value) function to convert the result to the requested [values-unit](values-unit).

## description

The sqrdist calculates faster than the [dist](dist) function and can be used if only the distance order is relevant.

## applies to

- *destination* and *origin* are data items with Point value type

## conditions

The values unit and domain unit of the *destination* and *origin* [argument](argument) must match.

## example

<pre>
attribute&lt;m2&gt; sqrdistOD (ADomain) := value(<B>sqrdist(</B>destination, origin<B>)</B>, m2);
</pre>

| destination      | origin           |**sqrdistOD**|
|------------------|------------------|------------:|
| {401331, 115135} | {401331, 115135} | **0**       |
| {399501, 111793} | {399476, 111803} | **725**     |
| {399339, 114883} | {399289, 114903} | **2900**    |
| {401804, 111323} | {401729, 111353} | **6525**    |
| {398796, 111701} | {398696, 111741} | **11600**   |

*ADomain, nr of rows = 5*

## see also

- [dist](dist)