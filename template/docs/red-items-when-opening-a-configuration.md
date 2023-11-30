---
title: red-items-when-opening-a-configuration
layout: default
nav_exclude: true
---
![](../assets/img/GUI/geodms_know_issue_missing_data.png)

When opening a project, it can occur that source data can not be read. Items become red and errors are generated.

This usually indicates the [folders-and-placeholders](folders-and-placeholders) [sourcedatadir](sourcedatadir) used in the configuration, refers to a folder on your local machine not containing the source data used in your project.

## solution

Open the Options dialog with the Tools > Options menu item in the [geodms-gui](geodms-gui). Activate the Advanced tab.

![](../assets/img/GUI/geodms_options_general.png)

The SourceDataDir control indicates to which folder on your local machine the SourceDataDir placeholder refers. There are two options to solve the issue:

1.  Move (or copy) the source data of your project on your local machine to the folder indicated in this control.
2.  Or adjust the value in the control, click OK, close the application and restart it to activate the new value.

Check also if the [localdatadir](localdatadir) control refers to an existing folder on your local machine with enough space. Do not configure a network drive as LocalDataDir.