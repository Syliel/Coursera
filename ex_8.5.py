#!/usr/bin/env python3

fname = input("Enter a file name: ")
fh = open(fname)
count = 0

for line in fh:
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[1])
    if line.startswith('From '):
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
