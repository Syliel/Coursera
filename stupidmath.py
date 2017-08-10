#!/usr/bin/env python3

hrs = input("Enter Hours:")
h = float(hrs)
base_hours = 40
rate = 10.50
ot_rate = rate * 1.5

if h > 40:
    ot_hours = h - 40

pay = ot_hours * ot_rate + base_hours * rate

print(pay)
