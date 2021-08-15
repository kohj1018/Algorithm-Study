N = int(input())
numList = list(map(int, input().split()))

minNum = numList[0]
maxNum = numList[0]

for i in range(N):
    if numList[i] < minNum:
        minNum = numList[i]
    elif numList[i] > maxNum:
        maxNum = numList[i]

print(minNum, maxNum, sep=' ')


# 파이썬의 내장함수 min(), max()를 써도 괜찮다고 한다.