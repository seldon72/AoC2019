#!/usr/bin/env python3

start = 178416
end = 676461
valid = 0

for i in range(start, end + 1):
    code = str(i)

    i = 0
    same = False
    bigger = True

    for num in code[1:]:
        if code[i] == num:
            same = True
        elif code[i] > num:
            bigger = False
            break
        i += 1
    
    if same and bigger:
        valid += 1

print(valid)
