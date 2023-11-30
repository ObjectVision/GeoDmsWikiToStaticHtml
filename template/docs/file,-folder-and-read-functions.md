---
title: file,-folder-and-read-functions
layout: default
parent: operator
nav_order: 46
---
File, Folder and Read [operators-and-functions](operators-and-functions) operate on files and folders, like [makedir](makedir) or [storage_name](storage_name) or read data in specific formats, like [readlines](readlines)

-   [existingfile](existingfile) - *full path name of the filename argument if the file exists and in the alternative argument if the file does not exists*
-   [createfile](createfile) - *copies the source filename to the target filename*
-   [initfile](initfile) - *copies the init filename to the target filename, synonym for CreateFile*
-   [copyfile](copyfile) - *copies the source filename to the target filename*

<!-- -->

-   [currentdir](currentdir) - *the folder of the root file of the loaded configuration*
-   [makedir](makedir) - *creates a new folder*
-   [fullpathname](fullpathname) - *full path name of the folder_or_filename argument*

<!-- -->

-   [exec](exec) - *executes a command argument*
-   [exec_ec](exec_ec) - *executes a command with a returning exitcode*
-   [execdll](execdll) - *executes a function in the dll*

<!-- -->

-   [storage_name](storage_name) - *value of the StorageName property*

<!-- -->

-   [readvalue](readvalue) - *a single parameter value from a string dataitem*
-   [readarray](readarray) - *an attribute, with row(s) of values from a string dataitem*
-   [readlines](readlines) - *an attribute with the concatenation of the values of the rows*
-   [readelems](readelems) - *an attribute, with column(s) of values from a string dataitem*

<!-- -->

-   [parse_xml](parse_xml) - *parses the contents of the argument with XML data into a set of configured attributes, based on the xml_scheme argument.*