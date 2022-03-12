"""
1. 아이디어
끝나는 시간을 기준으로 오름차순 정렬하고 그 다음 시작하는 시간을 기준으로 오름차순 정렬한다.
그리고 for문으로 돌려 앞전의 끝나는 시간과 현재 for문으로 들어온 회의의 시작 시간을 비교해 겹치지 않는다면
가져와 전체 회의 끝나는 시간을 현재 for문으로 들어온 회의의 끝나는 시간으로 바꾼다.

2. 시간복잡도
- O(nlgn) : 100000 * 16.6 = 1660000 < 4억    -> 가능

3. 자료구조
N: int;
info: int[][];
curEndTime: int;
maxCnt: int;
"""
import sys

input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

info.sort(key=lambda x: (x[1], x[0]))

maxCnt = 0
curEndTime = 0
for start, end in info:
    if curEndTime <= start:
        curEndTime = end
        maxCnt += 1


print(maxCnt)