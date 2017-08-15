#!/usr/bin/env python3
count = 0
total = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        ipos = line.find("0")
        piece = line[ipos:]
        value = float(piece)
        total = total + value
average = total / count
print(average)
