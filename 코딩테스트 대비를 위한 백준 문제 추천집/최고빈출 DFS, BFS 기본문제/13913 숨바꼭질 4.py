"""
1. 아이디어
BFS 탐색하면서 경로의 위치에 대한 배열도 큐에 넣고 확인하면 될 것 같다.

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
path = [0] * 100001

queue = deque()
queue.append(N)
road[N] = 1
while queue:
    popN = queue.popleft()
    if popN == K:
        print(road[K] - 1)
        pathResult = []
        while popN != N:
            pathResult.append(path[popN])
            popN = path[popN]
        pathResult.reverse()
        pathResult.append(K)
        print(" ".join(map(str, pathResult)))
        break
    for newN in (popN-1, popN+1, 2*popN):
        if 0<=newN<100001 and road[newN] == 0:
            road[newN] = road[popN] + 1
            path[newN] = popN
            queue.append(newN)


# 아래는 따로 path 배열을 안만들고 파라매터로 받아 처리한건데 시간초과 나온다...
# 왜 시간초과가 나올까..?
# queue = deque()
# queue.append([N])
# road[N] = 1
# while queue:
#     pathList = queue.popleft()
#     popN = pathList[-1]
#     if popN == K:
#         print(road[K]-1)
#         print(" ".join(map(str, pathList)))
#         break
#     for newN in (popN-1, popN+1, 2*popN):
#         if 0<=newN<100001 and road[newN] == 0:
#             road[newN] = road[popN] + 1
#             queue.append(pathList + [newN])
