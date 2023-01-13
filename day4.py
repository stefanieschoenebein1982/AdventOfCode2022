#!/usr/bin/env python3

with open('day4.txt') as f:
    contents = f.readlines()

# task 1
def completeOverlapExistsFor(firstElveMin, firstElveMax, secondElveMin, secondElveMax):
    print('Input: ' + str(firstElveMin) + ' ' + str(firstElveMax) + ' ' + str(secondElveMin) + ' ' + str(secondElveMax))
    if firstElveMin <= secondElveMin and firstElveMax >= secondElveMax:
        print('firstCase')
        print(firstElveMin + ' <= ' + secondElveMin + ' = true')
        print(firstElveMax + ' >= ' + secondElveMax + ' = true')
        print(' ')
        return True
    elif secondElveMin <= firstElveMin and secondElveMax >= firstElveMax:
        print('secondCase')
        print(secondElveMin + ' <= ' + firstElveMin + ' = true')
        print(secondElveMax + ' >= ' + firstElveMax + ' = true')
        print(' ')
        return True
    else:
        print('False')
        print(' ')
        return False

foundCompleteOverlapsCounter = 0
for line in contents:
    bothTasks = line.split(',')
    firstElveTasks = bothTasks[0].split('-')
    secondElveTasks = bothTasks[1].split('-')
    firstElveMin = firstElveTasks[0].strip()
    firstElveMax = firstElveTasks[1].strip()
    secondElveMin = secondElveTasks[0].strip()
    secondElveMax = secondElveTasks[1].strip()

    if completeOverlapExistsFor(firstElveMin, firstElveMax, secondElveMin, secondElveMax):
        foundCompleteOverlapsCounter += 1

print('Task1: ' + str(foundCompleteOverlapsCounter))
