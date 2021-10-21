#!/usr/bin/env python
# coding: utf-8

import os
import platform

def file_renamer():
    path = input("Path to the files to be renamed: ")
    extension = input("Choose extension of files: ")
    prefix = input ("Choose file prefix: ")
    x = 0

    if platform.system() == 'Windows':
        os.chdir(fr'{path}')
    else:
        os.chdir(path)

    for file in os.listdir():
        file = file.lower()
        if file.endswith(f'.{extension.lower()}'):
            x += 1
            os.rename(file, f'{prefix}_{x}.{extension.lower()}')

