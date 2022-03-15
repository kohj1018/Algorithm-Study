"""
1. 아이디어
순간이동하는 경우는 0초이므로 그때는 같은 초로 적어두고 bfs순회하면 될듯

2. 시간복잡도
- O(N)

3. 자료구조
N, K: int;
road: int[];
"""
import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
road = [0] * 100001

queue = deque()
queue.append(N)
road[N] = 1
while queue:
    popN = queue.popleft()
    if popN == K:
        print(road[K]-1)
        break
    for newN in (2*popN, popN-1, popN+1):
        if 0 <= newN < 100001 and road[newN] == 0:
            if newN == 2*popN:      # 순간 이동 하는 경우
                road[newN] = road[popN]
                queue.appendleft(newN)
            else:                   # 걸어서 이동 하는 경우
                road[newN] = road[popN] + 1
                queue.append(newN)