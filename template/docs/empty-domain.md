---
title: empty-domain
layout: default
nav_exclude: true
---
An empty domain is a [domain-unit](domain-unit) with zero elements.

The following example shows how such a domain and a set of [attribute](attribute) for this domain can be configured.

<pre>
unit&lt;uint32&gt; empty_domain : nrofrows = 0
{
   attribute&lt;uint32&gt; int_data         : [ ];
   attribute&lt;dpoint&gt; poly_data (poly) : [ ];
}
</pre>