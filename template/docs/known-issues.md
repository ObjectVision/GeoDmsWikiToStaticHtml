---
title: known-issues
layout: default
parent: software
nav_order: 13
---
## disabled items not greyed out, look like enabled
This can happen if the 'dark mode' is enabled in Windows 11. Reconsider using the 'dark mode'.

## clear the CalcCache
For GeoDMS versions prior to the 8 serie, if an error occurs with a running a GeoDMS project or re-opening a current configuration, we first advice to clear the CalcCache folder. 

## memory issues
In case your computer runs out of (virtual) memory, the user can adapt their Windows OS settings of [virtual-memory](virtual-memory) in order to deal with memory issues. Alternatively, as secondary option disabling Multi Tasking option 2 (From the GUI go to Tools \> Options \> Advanced) can be unchecked. Be aware that calculations that make use of multiple threads will become slower.

## other issues

-   [msvcp110_win.dll missing](https://answers.microsoft.com/en-us/windows/forum/all/cwindowssystem32msvcp110windll-error/ecc76238-a2ce-4711-a714-ff639c926597?auth=1)
-   [vcruntime140-1-dll-missing](vcruntime140-1-dll-missing)
-   [api-ms-win-crt-runtime-i1-1-0.dll-is-missing](api-ms-win-crt-runtime-i1-1-0.dll-is-missing)
-   [red-items-when-opening-a-configuration](red-items-when-opening-a-configuration)
-   [windowssystem-error-createfilehandleforrwview-errorcode-32...](windowssystem-error-createfilehandleforrwview-errorcode-32...)
-   [error-in-delayed-loading-a-dll](error-in-delayed-loading-a-dll)
-   [notepad---command-line-parameters-not-working](notepad---command-line-parameters-not-working)