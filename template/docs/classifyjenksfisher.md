---
title: classifyjenksfisher
layout: default
nav_exclude: true
---
*[classify-functions](classify-functions) ClassifyJenksFisher*

## syntax

- ClassifyJenksFisher(*a*, *[domain-unit](domain-unit)*)

## definition

ClassifyJenksFisher(*a*, *domain unit*) results in a [data-item](data-item) with class breaks, based on the method described in [fisher's-natural-breaks-classification-complexity-proof](fisher's-natural-breaks-classification-complexity-proof).
The resulting [values-unit](values-unit) is the values unit of data item *a*, the resulting [domain-unit](domain-unit) is the *domain unit* [argument](argument).

- *a*: numeric data item to be classified
- *domain unit*: determining the number of class breaks.

## description

The Jenks Fisher classification method, is a fast algorithm that results in breaks that minimize the sum of the square deviations from the class means, also known as natural breaks. The self contained code with an example usage is:
[calcnaturalbreaks](calcnaturalbreaks)

The same function can also be applied from the [geodms-gui](geodms-gui) by requesting the Palette Editor of a map layer and activate the Classify > JenksFisher classification.

The ClassifyJenksFisher results in a set of ClassBreaks that can be used in the [classify](classify) function to classify a data item.

## applies to

- data item a with Numeric [value-type](value-type)
- domain unit with value type from group CanBeDomainUnit

## since version

7.019

## example

<pre>
attribute&lt;nrPersons&gt; classifyJfNrInh (inh_4K) := <B>ClassifyJenksFisher(</B>NrInh, inh_4K<B>)</B>;
</pre>

| **classifyJfNrInh** |
|--------------------:|
| **0**               |
| **200**             |
| **550**             |
| **860**             |

*Table inh_4K, nr of rows = 4*


| NrInh |
|------:|
| 550   |
| 1025  |
| 300   |
| 200   |
| 0     |
| null  |
| 300   |
| 2     |
| 20    |
| 55    |
| 860   |
| 1025  |
| 1025  |
| 100   |
| 750   |

*Table District, nr of rows = 15*

see also
- [classifynonzerojenksfisher](classifynonzerojenksfisher)