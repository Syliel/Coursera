#!/usr/bin/env python3

HRS = float(input("Enter your hours: "))
RATE = float(input("Enter the rate of pay: "))
BASE_HOURS = 40
OT_RATE = RATE * 1.5

def computerate(hrs, rate):
    ot_hours = 0
    if hrs > 40:
        ot_hours = hrs - 40
    return ot_hours * OT_RATE + BASE_HOURS * rate

result = computerate(HRS, RATE)
print(result)
