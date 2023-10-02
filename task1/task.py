numList = [11, 2, 51, 4, 0, 4, 1]

def sortListImperative(numList):
    n = len(numList)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numList[j] < numList[j + 1]:
                numList[j], numList[j + 1] = numList[j + 1], numList[j]
    return numList


def sortListDeclarative(numList):
    return sorted(numList, reverse=True)


print(sortListImperative(numList))
print(sortListDeclarative(numList))
