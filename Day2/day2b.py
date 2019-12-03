#! /usr/bin/env python3

def run_program(noun, verb, code):
    code[1] = noun
    code[2] = verb
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

    return code[0]

with open("input") as f:
    for line in f:
        program = [int(s) for s in line.split(',')]


output = 19690720
for i in range(100):
    for j in range(100):
        if run_program(i, j, program[:]) == output:
            print(100 * i + j)
            break



