#!/usr/bin/env python3

total = 0
print("Before", total)
for thing in [9, 41, 12, 3, 74, 15]:
    total = total + thing
    print(total, thing)
print("After", total)
