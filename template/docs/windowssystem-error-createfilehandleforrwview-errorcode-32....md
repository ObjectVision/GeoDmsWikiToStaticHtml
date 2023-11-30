---
title: windowssystem-error-createfilehandleforrwview-errorcode-32...
layout: default
nav_exclude: true
---
If another instance of the GeoDMS (GUI or batch) for the same project is already running, an error like the following is generated:

![](../assets/img/GUI/geodms_know_issue_running_instance.png)

The running instance locks the CalcCache, this locking results in the presented error.

## solution

Do not run the same project twice, wait for the first instance is finished before rerunning.