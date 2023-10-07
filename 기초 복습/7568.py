"""
1. 아아디어
자신보다 덩치가 큰 사람을 구해서 +1로 출력해주면 된다.

2. 시간 복잡도
- O(N^2) : 50 * 50 = 2500   -> 가능

3. 변수
덩치 리스트 : int[][]
"""
import sys

input = sys.stdin.readline

N = int(input())

big = []
for _ in range(N):
    x, y = map(int, input().split())
    big.append([x, y])

for i in big:
    biggerNum = 1
    for j in big:
        if i != j:
            if i[0] < j[0] and i[1] < j[1]:
                biggerNum += 1
    print(biggerNum, end=' ')