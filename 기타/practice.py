import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

""""""""""""""""""""""""""""""""""""""""""
N, K = map(int, input().split())

road = [0 for _ in range(100001)]
path = [-1 for _ in range(100001)]

queue = deque()
queue.append(N)
road[N] = 1
while queue:
    popN = queue.popleft()
    if popN == K:
        print(road[K] - 1)
        i = K
        pathResult = []
        while path[i] != -1:
            pathResult.append(i)
            i = path[i]
        pathResult.append(N)
        pathResult.reverse()
        print(" ".join(map(str, pathResult)))
        break
    for nextN in (popN-1, popN+1, 2*popN):
        if 0<=nextN<100001 and road[nextN] == 0:
            road[nextN] = road[popN] + 1
            path[nextN] = popN
            queue.append(nextN)
