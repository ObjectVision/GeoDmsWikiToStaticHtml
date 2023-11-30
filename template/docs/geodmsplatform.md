---
title: geodmsplatform
layout: default
nav_exclude: true
---
*[miscellaneous-functions](miscellaneous-functions) GeoDmsPlatform*

**This function is Obsolete since v8.7.0.**

## syntax

- GeoDmsPlatform()

## definition

GeoDmsPlatform() results in a string [parameter](parameter) indicating if the running GeoDMS executable is a **Win32 or X64 version**.

## example

<pre>
parameter&lt;string&gt; GeoDmsPlatform := <B>GeoDmsPlatform();</B>
</pre>
*result: GeoDmsPlatform = Win32 or GeoDmsPlatform = X64*