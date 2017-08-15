#!/usr/bin/env python3

text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find("0")
piece = text[ipos:]
value = float(piece)
print(value)
