---
title: execdll
layout: default
nav_exclude: true
---
*[file,-folder-and-read-functions](file,-folder-and-read-functions) exec(ute)Dll*

## syntax

- execDll(*dll*, *function*)

## definition

execDll(*dll*, *function*) **executes the *function* in the *dll***.

## applies to

- dll and function with string [value-type](value-type)

## example

<pre>
container execDll := <B>execDll(</B>'C:/dev/bin/accessrun.dll','RunProcAndWait'<B>)</B>;
</pre>

## see also

- [exec](exec)
- [exec_ec](exec_ec)