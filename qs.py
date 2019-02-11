# -*- coding: utf-8 -*-
import time

def quickSort(listToSort):
    if len(listToSort) == 1 or len(listToSort) == 0:
        return listToSort
    elif len(listToSort) == 2:
        if listToSort[0] > listToSort[1]:
            temp = listToSort[0]
            listToSort[0] = listToSort[1]
            listToSort[1] = temp
        return listToSort

    midNum = listToSort[0] # Seleting a middle number
    currentIndex = 0 # Record the current index of the middle number
    for i in range(1,len(listToSort)): # iterating through the rest of the array
        if listToSort[i] < midNum:
            temp = listToSort[i]
            for j in reversed(range(currentIndex,i)): # moving previous elements up a space for this number to go to the front
                listToSort[j + 1] = listToSort[j]
            listToSort[currentIndex] = temp
            currentIndex += 1
    # Split the array into two and start recursion
    return quickSort(listToSort[0:currentIndex]) + [midNum] + quickSort(listToSort[currentIndex+1:])

def mergeSort(listToSort):
    if len(listToSort) == 1:
        return listToSort
    elif len(listToSort) == 2:
        if listToSort[0] > listToSort[1]:
            temp = listToSort[0]
            listToSort[0] = listToSort[1]
            listToSort[1] = temp
            return listToSort
    
    # split the array into two small parts, and merge them together
    halfLen = len(listToSort) // 2
    part1 = listToSort[0:halfLen]
    part2 = listToSort[halfLen:]
    # if len is odd, part2 has 1 more element than part1
    
    #start recursion
    part1 = mergeSort(part1)
    part2 = mergeSort(part2)

    rstArray = []
    #finish recursion, merging arrays.
    while len(part1) > 0 or len(part2) > 0:
        if len(part1) > 0 and len(part2) > 0:
            if part1[0] > part2[0]:
                rstArray.append(part2[0])
                part2.pop(0)
            else:
                rstArray.append(part1[0])
                part1.pop(0)
        else:
            rstArray += part1 + part2
            part1 = []
            part2 = []
    
    #finish merging
    return rstArray

quickSortCases = {
    "largeN": {
        "best": [11,5,3,8,16,14,18,1,6,12,17,2,7,13,19,4,9,15,20,10],
        "worst": list(range(1,21)),
        "random": [9,11,4,1,17,20,3,5,12,2,7,6,19,13,14,16,10,18,15,8]
    },
    "smallestN": {
        "best": [5,3,8,1,2,4,6,7,9,10],
        "worst": list(range(1,11)),
        "random": [3,5,9,6,1,2,4,10,8,7]
    },
    "name": "QuickSort"
}
mergeSortCases = {
    "largeN": {
        "best": list(range(1,21)),
        "worst": [9,1,17,5,13,11,19,3,7,15,10,2,18,6,14,12,4,20,8,16],
        "random": [9,11,4,1,17,20,3,5,12,2,7,6,19,13,14,16,10,18,15,8]
    },
    "smallestN": {
        "best": list(range(1,11)),
        "worst": [3,7,5,1,9,4,8,6,2,10],
        "random": [3,5,9,6,1,2,4,10,8,7]
    },
    "name": "MergeSort"
}

for i in range(0,2):
    case = {}
    if i==0:
        case = quickSortCases
    elif i == 1:
        case = mergeSortCases
    for j in range(0,2):
        Nkey = ''
        if j == 0:
            Nkey = 'largeN'
        elif j==1:
            Nkey = "smallestN"
        for h in range(0,3):
            caseKey = ''
            if h==0:
                caseKey = 'best'
            elif h==1:
                caseKey = 'worst'
            else: #h==2
                caseKey = 'random'
            print("sorting using " + case['name'] + ", N = " + Nkey + ", case = " + caseKey)
            print("dataSet: ")
            print(case[Nkey][caseKey])
            print("-----------------------------------------------------------")
            startTime = time.clock()
            result = []
            if i==0:
                result = quickSort(case[Nkey][caseKey])
            elif i==1:
                result = mergeSort(case[Nkey][caseKey])
            print("timeElapsed: " + str(time.clock() - startTime))
            print("sortedSet:")
            print(result)
            print("-----------------------------------------------------------")
            print()
        