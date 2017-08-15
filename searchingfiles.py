#!/usr/bin/env python3

fhand = open('words.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
