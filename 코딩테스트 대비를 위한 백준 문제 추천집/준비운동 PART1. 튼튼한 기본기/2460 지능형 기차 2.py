maxNum = 0
curNum = 0
for _ in range(10):
    outNum, inNum = map(int, input().split())
    curNum += inNum - outNum
    if curNum > maxNum:
        maxNum = curNum

print(maxNum)