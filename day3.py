#!/usr/bin/env python3

def findCommonCharacter(firstString, secondString):
    for character in firstString:
        for index in range(len(secondString)):
            if character == secondString[index]:
                return character

def mapCharacterToNumber(character):
    if character.islower():
        return ord(character) - 96
    else:
        return ord(character) - 38

with open('day3.txt') as f:
    contents = f.readlines()

# task 1
sumOfPriorities = 0
for line in contents:
    stringLenght = len(line)
    string1 = line[slice(0,stringLenght//2)]
    string2 = line[slice(stringLenght//2,stringLenght)]
    sumOfPriorities += mapCharacterToNumber(findCommonCharacter(string1, string2))
print('result Task1: ' + str(sumOfPriorities))

def findCommonCharacterFromThreeElves(one, two, three):
    for character in one:
        for index in range(len(two)):
            if character == two[index]:
                for innerIndex in range(len(three)):
                    if character == three[innerIndex]:
                        return character

# task 2
index = 0
sumOfPrioritiesTask2 = 0

while(index < len(contents)):
    print('Start with Index:' + str(index))
    firstElve = contents[index + 0]
    secondElve = contents[index + 1]
    thirdElve = contents[index + 2]

    commonCharacter = findCommonCharacterFromThreeElves(firstElve, secondElve, thirdElve)
    sumOfPrioritiesTask2 += mapCharacterToNumber(commonCharacter)
    index += 3

print('result Task2: ' + str(sumOfPrioritiesTask2))
