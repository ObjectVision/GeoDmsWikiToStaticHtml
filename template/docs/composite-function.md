---
title: composite-function
layout: default
nav_exclude: true
---
## definition

Composite functions are functions generating one or more subitems (e.g. [select_with_org_rel](select_with_org_rel), [griddist](griddist))

## caching

The direct results (generated [subitem](subitem)) are [session-specific](session-specific).

Indirect results, calculated with expressions that are not only direct references to such subitems can be stored persistently.

In this way they differ from the session-specific functions.