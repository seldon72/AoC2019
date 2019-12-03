#! /usr/bin/env python3

with open("input") as f:
    for line in f:
        code = [int(s) for s in line.split(',')]

code[1] = 12
code[2] = 2
start = 0
end = 0

while end != 99:

    intcode = code[start:start + 4]

    if intcode[0] == 1:
        code[intcode[3]] = code[intcode[1]] + code[intcode[2]]
    elif intcode[0] == 2:
        code[intcode[3]] = code[intcode[1]] * code[intcode[2]]

    start += 4
    end = code[start]

print(code)

