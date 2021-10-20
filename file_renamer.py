#!/usr/bin/env python
# coding: utf-8

extension = input("Choose extension of files: ")
prefix = input ("Choose file prefix: ")
x = 0

for file in os.listdir():
    file = file.lower()
    if file.endswith(f'.{extension.lower()}'):
        x += 1
        os.rename(file, f'{prefix}_{x}.{extension.lower()}')
        

