ninja-ide-autopepper-plugin
===========================

Plugin for reformating to PEP8 compliant syntax


This plugins allows you to have your code pretty-printed according to PEP8 by pressing CTRL+P.
It uses autopep8 as a library under the hood.

Known problems
---------------
+ The history has a blank state in between the "meessy" and the "pretty" version - this is due to the fact that there is no "instant" replacement method for all the buffer contet of the QText Control :-(


Current-Version: 0.3

Version History
---------------
0.1 - initial introduction
0.2 - fixed error in json-plugin description leading to a freeze at startup
0.3 - fixed the shortcut, changed it to CTRL+SHIFT+P (CTRL+P was printing)
    - fixed the menu item