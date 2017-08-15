#!/usr/bin/env python3

fname = input("Enter a file name: ")
fh = open(fname)
for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
