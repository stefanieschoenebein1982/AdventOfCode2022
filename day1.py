#!/usr/bin/env python3

with open('day1.txt') as f:
    contents = f.readlines()

separatedByEmptyLine = [[]]
number = 0
for line in contents:
    if line == '\n':
        number += 1
        separatedByEmptyLine.append([])
    else:
        separatedByEmptyLine[number].append(int(line.strip()))

elvesSum = []
for elves in separatedByEmptyLine:
    elvesSum.append(sum(elves))

threeHighest = []
for index in range(3):
    threeHighest.append(max(elvesSum))
    elvesSum.remove(max(elvesSum))
print (sum(threeHighest))
