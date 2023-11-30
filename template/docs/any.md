---
title: any
layout: default
nav_exclude: true
---
*[aggregation-functions](aggregation-functions) any*

## syntax

- any(*a*)
- any(*a*, *relation*)

## definition

1. any(*a*) results in a boolean [parameter](parameter), with the value True if **any** value of boolean [attribute](attribute) *a* is True and the value False    in all other cases.
2. any(*a*, *relation*) results in a boolean [attribute](attribute), with the values True if **any** value of boolean [attribute](attribute) *a* is True and as values False in all other cases, grouped by *[relation](relation)*. The [domain-unit](domain-unit) of the resulting attribute is the [values-unit](values-unit) of the *relation*.

## applies to

- [attribute](attribute) *a* with bool [value-type](value-type)
- *[relation](relation)* with value type of the group CanBeDomainUnit

## conditions

The domain of [argument](argument) *a* and *relation* must match.

## example

<pre>
parameter&lt;bool&gt; anyA := <B>any(</B>A<B>)</B>; result = True
parameter&lt;bool&gt; anyB := <B>any(</B>B<B>)</B>; result = True
parameter&lt;bool&gt; anyC := <B>any(</B>C<B>)</B>; result = False
</pre>

| **A**    | **B**     | **C**     |
|----------|-----------|-----------|
| **True** | **True**  | **False** |
| **True** | **False** | **False** |
| **True** | **True**  | **False** |
| **True** | **False** | **False** |
| **True** | **True**  | **False** |

*ADomain, nr of rows = 5*

## see also

- [all](all)