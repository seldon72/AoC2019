#! /usr/bin/env python3

def fuel(amt):
    return (amt//3) - 2

def all_fuel(amt):
    num = fuel(amt)
    sub = 0
    while num > 0:
        sub += num
        num = fuel(num)
    
    return sub
    

total = 0 
with open("input") as f:
    for line in f:
        total += all_fuel(int(line))

print(total)


