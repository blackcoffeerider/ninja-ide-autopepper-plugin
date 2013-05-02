ninja-ide-autopepper-plugin
===========================

Plugin for reformating to PEP8 compliant syntax


This plugins allows you to have your code pretty-printed according to PEP8 by pressing CTRL+P.
It uses autopep8 as a library under the hood.

Known problems
---------------
+ Shortcut is not configurable
+ Toolbar doesn't work - altough code is executed
+ The history has a blank state in between the "meessy" and the "pretty" version - this is due to the fact that there is no "instant" replacement method for all the buffer contet of the QText Control :-(


Current-Version: 0.2

Version History
---------------
0.1 - initial introduction
0.2 - fixed error in json-plugin description leading to a freeze at startup