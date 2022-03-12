"""
1. 아이디어
오름차순 정렬한 뒤 더해 나가기

2. 시간복잡도
- O(N)

3. 자료구조
N: int;
PList: int[];
requireTime: int;
result: int;
"""
import sys

input = sys.stdin.readline

N = int(input())
PList = list(map(int, input().split()))
PList.sort()

requireTime = 0
result = 0
for time in PList:
    requireTime += time
    result += requireTime


print(result)
