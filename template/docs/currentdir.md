---
title: currentdir
layout: default
nav_exclude: true
---
*[file,-folder-and-read-functions](file,-folder-and-read-functions) CurrentDir(ectory)*

## syntax

- CurrentDir()

## definition

- CurrentDir() results in a string [parameter](parameter) with the **folder of the root file of the loaded configuration**.

## example

parameter&lt;string&gt; cdir := <B>CurrentDir()</B>;

*result: cdir = 'c:/data/dev/prj/tst/Operator/cfg*'