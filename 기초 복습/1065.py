"""
1. 아이디어
N까지 for문 돌리고 숫자를 문자열로 받아 각자리수의 차를 비교해 맞으면 카운트

2. 시간복잡도
O(4*N) : 4 * 1,000 = 4,000 < 2억     -> 가능

3. 자료구조
"""
import sys

input = sys.stdin.readline

N = int(input())

cnt = 0
for i in range(1, N + 1):
    if i > 99:
        isHanNum = True
        standardDiff = int(str(i)[0]) - int(str(i)[1])
        for j in range(1, len(str(i)) - 1):
            diff = int(str(i)[j]) - int(str(i)[j + 1])
            if standardDiff != diff:
                isHanNum = False
                break
        if isHanNum:
            cnt += 1

    else:
        cnt += 1

print(cnt)
