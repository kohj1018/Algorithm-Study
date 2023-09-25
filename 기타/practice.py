import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

""""""""""""""""""""""""""""""""""""""""""
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())
edge = [[] for _ in range(V + 1)]
dist = [INF for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    edge[u].append([w, v])

dist[K] = 0
heap = [[0, K]]
while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew: continue
    for nw, nv in edge[ev]:
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, [dist[nv], nv])


for i in range(1, V + 1):
    if dist[i] == INF: print("INF")
    else: print(dist[i])