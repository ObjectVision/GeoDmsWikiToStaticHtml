---
title: exec
layout: default
nav_exclude: true
---
*[file,-folder-and-read-functions](file,-folder-and-read-functions) exec(ute)*

## syntax

- exec(*command*)

## definition

exec(*command*) **executes** the *command* [argument](argument).

if the results of the exec command (for instance a list of files to be imported) are used further in the process, use the [exec_ec](exec_ec) function to make sure the command is executed or an error code is generated.

## applies to

- *command* with string [value-type](value-type)

## example

container calc := <B>exec(</B>'calc.exe'<B>)</B>;

<I>result: runs the Windows calculator</I>

## see also

- [exec_ec](exec_ec)
- [execdll](execdll)