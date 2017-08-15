#!/usr/bin/env python3

name = input('Enter a file: ')
handle = open(name)
bigcount = None
counts = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    if line.startswith('From '):
        words = line.split()
        pieces = words[1]
        counts[pieces] = counts.get(pieces, 0) + 1
        for pieces,count in counts.items():
            if bigcount is None or count > bigcount:
                bigword = pieces
                bigcount = count

print(bigword, bigcount)

