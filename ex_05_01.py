#!/usr/bin/env python3

num = 0
tot = 0.0
while True:
    sval = input("Enter a number or 'done' to finish: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invalid input")
        continue
    num = num + 1
    tot = tot + fval

print("All done")
print(tot, num, tot/num)
