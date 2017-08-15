#!/usr/bin/env python3

name = input("Enter file: ")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    pieces = words[5]
    smaller = pieces[:2]
    counts[smaller] = counts.get(smaller, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (key, val)
    lst.append(newtup)
lst = sorted(lst, reverse=False)

for key, val in lst:
    print(key, val)

