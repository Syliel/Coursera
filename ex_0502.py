#!/usr/bin/env python3

largest = None
smallest = None
while True:
    num = input("Enter a number or done to quit:")
    if num == "done":
        break
    try:
        fval = int(num)
    except:
        print("Invalid input")
        continue

    if smallest is None:
        smallest = fval
    elif fval < smallest:
        smallest = fval
    
    if largest is None:
        largest = fval
    elif fval > largest:
        largest = fval

print("Maximum", largest)
print("Minimum", smallest)
