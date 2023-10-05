"""
1. 아이디어
- 각 별의 자리 좌표를 받은 후 각각의 별들을 잇는 간선의 가중치를 모두 구한다. (모든 별은 간선으로 이어져 있다고 가정)
- 이후 해당 가중치를 이용해 MST로 별자리 만드는 최소 비용을 구한다.

2. 시간복잡도
- 모든 별 간의 가중치 구하는 비용 : O(n^2) -> 100 * 100 = 10,000
- MST : O(ElgE) = n^2 * lg(n^2) = 10000 * lg(10000) = 4,0000    -> 가능

3. 변수
- 별 위치 배열 : float[][]
- 인접 리스트 : float[][]
- 방문 여부 : bool[]
- 별자리 만드는 비용 : float
"""
import sys
import math
import heapq

input = sys.stdin.readline

n = int(input())

edge = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)

node = [[0, 0]]
for _ in range(n):
    x, y = map(float, input().split())
    node.append([x, y])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j:
            dist = round(math.sqrt((node[i][0] - node[j][0]) ** 2 + (node[i][1] - node[j][1]) ** 2), 2)
            edge[i].append([dist, j])

heap = [[0, 1]]
cost = 0

while heap:
    w, v = heapq.heappop(heap)
    if not visit[v]:
        visit[v] = True
        cost += w
        for nw, nv in edge[v]:
            if not visit[nv]:
                heapq.heappush(heap, [nw, nv])

print(cost)