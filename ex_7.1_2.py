#!/usr/bin/env python3
fname = input("Enter filename: ")
[print(s.rstrip().upper()) for s in open(fname)]
