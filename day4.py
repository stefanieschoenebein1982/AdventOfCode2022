#!/usr/bin/env python3

with open('day4.txt') as f:
    contents = f.readlines()

# task 1
def completeOverlapExistsFor(firstElveMin, firstElveMax, secondElveMin, secondElveMax):
    if firstElveMin <= secondElveMin and firstElveMax >= secondElveMax:
        return True
    elif secondElveMin <= firstElveMin and secondElveMax >= firstElveMax:
        return True
    else:
        return False

foundCompleteOverlapsCounter = 0
for line in contents:
    bothTasks = line.split(',')
    firstElveTasks = bothTasks[0].split('-')
    secondElveTasks = bothTasks[1].split('-')
    firstElveMin = int(firstElveTasks[0].strip())
    firstElveMax = int(firstElveTasks[1].strip())
    secondElveMin = int(secondElveTasks[0].strip())
    secondElveMax = int(secondElveTasks[1].strip())

    if completeOverlapExistsFor(firstElveMin, firstElveMax, secondElveMin, secondElveMax):
        foundCompleteOverlapsCounter += 1

print('Task1: ' + str(foundCompleteOverlapsCounter))
