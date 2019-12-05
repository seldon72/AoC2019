#! /usr/bin/env python3

array = []
with open("input") as f:
    for line in f:
        i = 0
        j = 0
        temp = []
        for s in line.split(','):
            if s[0] == 'R':
                r = i + 1
                i = i + int(s[1:])
                for x in range(r, i, 1):
                    temp.append(str(x) + ',' + str(j))
            elif s[0] == 'L':
                r = i - 1
                i = i - int(s[1:])
                for x in range(r, i, -1):
                    temp.append(str(x) + ',' + str(j))
            elif s[0] == 'U':
                r = j + 1
                j = j + int(s[1:])
                for y in range(r, j, 1):
                    temp.append(str(i) + ',' + str(y))
            elif s[0] == 'D':
                r = j - 1
                j = j - int(s[1:])
                for y in range(r, j, -1):
                    temp.append(str(i) + ',' + str(y))

        array.append(temp)    

smaller = 10000
for res in set(array[0]) & set(array[1]):
    value = (abs(int(res.split(',')[0]))) + (abs(int(res.split(',')[1])))
    if value < smaller:
        smaller = value

print(smaller)
        



