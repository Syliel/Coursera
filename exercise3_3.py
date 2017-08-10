#!/usr/bin/env python3

score = input("Enter Score: ")
try:
    score = float(score)
except: 
    print("Please enter a numerical value.")
    exit()

if score > 1.0:
    print("Score must be between 0.0 and 1.0")
elif score >= 0.9:
    score = "A"
elif score >= 0.8:
    score = "B"
elif score >= 0.7:
    score = "C"
elif score >= 0.6:
    score = "D"
elif score < 0.6 and score >= 0.0:
    score = "F"
else:
    print("score must be between 0.0 and 1.0")


print(score)
