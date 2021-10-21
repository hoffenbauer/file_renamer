# File renamer

This is a very simple function intented to be used as a mass file renamer. At the present version, it will rename all files in the folder ending with the chosen extension (e.g.: all PNGs in the selected folder will be renamed). Path, extension and prefix are provided via input.

It uses **platform** for detecting if the system is Windows, given the difference in path in relation to Unix systems.

The prefix is chosen by the user and a counter will increase according to the number of files.
