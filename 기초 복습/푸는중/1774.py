"""
1. 아이디어
- MST

2. 시간 복잡도
- O(V+E) : N + M = 1000 + 1000      -> 가능

3. 변수
- N, M : int
- 인접 리스트 : (통로 길이, 우주신 번호)[][]
- 힙 : (통로 길이, 우주신 번호)[]
- 방문 여부 : bool[]
"""
import sys
import math
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

node = [[0, 0]]

for _ in range(N):
    X, Y = map(int, input().split())
    node.append([X, Y])

edge = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j:
            edge[i].append([math.sqrt(math.pow(node[i][0] - node[j][0], 2) + math.pow(node[i][1] - node[j][1], 2)), j])

visit = [False] * (N + 1)
heap = []

for _ in range(M):
    v1, v2 = map(int, input().split())
    visit[v1] = True
    visit[v2] = True
    for nw, nv in edge[v1]:
        if not visit[nv]:
            heap.append([nw, nv])
    for nw, nv in edge[v2]:
        if not visit[nv]:
            heap.append([nw, nv])


min_dist = 0

while heap:
    w, v = heapq.heappop(heap)
    if not visit[v]:
        visit[v] = True
        min_dist += w
        for nw, nv in edge[v]:
            if not visit[nv]:
                heapq.heappush(heap, [nw, nv])

print("{:.2f}".format(min_dist))
