# """
# 1. 아이디어
# - 플로이드로 전체 마을 사이의 최단 경로를 구한다.
#     - 이중 for문으로 도로의 길이의 합이 가장 작은 사이클을 찾는다.
#
# 2. 시간 복잡도
# - O(V^3 + V^2) : 400 ^ 3 ~= 6억
#
# 3. 변수
# - V, E : int
# - dist : int[][]
# - min_dist : int
# """
# import sys
# INF = sys.maxsize
#
# input = sys.stdin.readline
#
# V, E = map(int, input().split())
#
# dist = [[INF] * (V + 1) for _ in range(V + 1)]
#
# for l in range(1, V + 1):
#     dist[l][l] = 0
#
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     dist[a][b] = min(dist[a][b], c)
#
# for k in range(1, V + 1):
#     for i in range(1, V + 1):
#         for j in range(1, V + 1):
#             if dist[i][j] > dist[i][k] + dist[k][j]:
#                 dist[i][j] = dist[i][k] + dist[k][j]
#
# min_dist = INF
# for a in range(1, V + 1):
#     for b in range(1, V + 1):
#         if a != b and dist[a][b] < INF - 1 and dist[b][a] < INF - 1:
#             if min_dist > dist[a][b] + dist[b][a]:
#                 min_dist = dist[a][b] + dist[b][a]
#
# if min_dist > INF - 1:
#     print(-1)
# else:
#     print(min_dist)

# 두번째 풀이 (Python3 시간 초과 해결)
"""
1. 아이디어
- 다익스트라를 변형하여 이용한다.
    - heap에 출발 노드까지 포함된 요소들로 초기 값에 가능한 모든 edge들을 넣어놓고 시작한다. (ElgV)
    - while문에 break를 추가해 소요 시간을 줄일 수 있도록 한다.

2. 시간 복잡도
- O(ElgV) : V^2 * lgV = 400^2 * lg(400) ~= 400,000      -> 가능

3. 변수
- V, E : int
- heap : (거리, 출발 마을, 도착 마을)
- 인접 리스트 : (거리, 도착 마을)
- 최단 거리 : int[][]
"""
import sys
import heapq
INF = sys.maxsize

input = sys.stdin.readline

V, E = map(int, input().split())

dist = [[INF] * (V + 1) for _ in range(V + 1)]  # 사이클을 구해야하므로 자기 자신한테 가는 최단거리를 0으로 세팅해두지 않음

heap = []
edge = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
    edge[a].append([c, b])
    heapq.heappush(heap, [c, a, b])

while heap:
    w, s, g = heapq.heappop(heap)
    if s == g:
        print(w)
        break
    if w != dist[s][g]: continue
    for nw, ng in edge[g]:
        if dist[s][ng] > dist[s][g] + nw:
            dist[s][ng] = dist[s][g] + nw
            heapq.heappush(heap, [dist[s][ng], s, ng])
else:
    print(-1)