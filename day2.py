#!/usr/bin/env python3

with open('day2_input.txt') as f:
    contents = f.readlines()
myScorePart1 = 0
for line in contents:
    opponent = line[0]
    me = line [2]
    if opponent == 'A':
        if me == 'Z':
            myScorePart1 += 3
        elif me == 'X':
            myScorePart1 += 4
        elif me == 'Y':
            myScorePart1 += 8
    elif opponent == 'B':
        if me == 'Z':
            myScorePart1 += 9
        elif me == 'X':
            myScorePart1 += 1
        elif me == 'Y':
            myScorePart1 += 5
    elif opponent == 'C':
        if me == 'Z':
            myScorePart1 += 6
        elif me == 'X':
            myScorePart1 += 7
        elif me == 'Y':
            myScorePart1 += 2
print(myScorePart1)

myScorePart2 = 0
for line in contents:
    opponent = line[0]
    me = line [2]
    if opponent == 'A':
        if me == 'Z':
            myScorePart2 += 8
        elif me == 'X':
            myScorePart2 += 3
        elif me == 'Y':
            myScorePart2 += 4
    elif opponent == 'B':
        if me == 'Z':
            myScorePart2 += 9
        elif me == 'X':
            myScorePart2 += 1
        elif me == 'Y':
            myScorePart2 += 5
    elif opponent == 'C':
        if me == 'Z':
            myScorePart2 += 7
        elif me == 'X':
            myScorePart2 += 2
        elif me == 'Y':
            myScorePart2 += 6

print(myScorePart2)

"""
    A Rock X 1
    B Paper Y 2
    C Scissor Z 3

    loss 0 X
    draw 3 Y
    win 6 Z

    A > Z   3
    A == X  4
    A < Y   8

    B > X   1
    B == Y  5
    B < Z   9

    C > Y   2
    C == Z  6
    C < X   7
"""
