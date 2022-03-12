def quickSort(numList):
    if len(numList) == 0:
        return []
    if len(numList) == 1:
        return [numList[0]]
    pivot = numList[0]
    leftList = []
    rightList = []
    for num in numList[1:]:
        if num < pivot:
            leftList.append(num)
        else:
            rightList.append(num)
    return quickSort(leftList) + [pivot] + quickSort(rightList)


T = int(input())
for _ in range(T):
    numList = list(map(int, input().split()))
    numList = quickSort(numList)
    print(numList[-3])