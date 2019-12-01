#! /usr/bin/env python3

total = 0 
with open("input") as f:
    for line in f:
        total += (int(line)//3) - 2

print(total)
