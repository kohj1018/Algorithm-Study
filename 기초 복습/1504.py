"""
1. 아이디어
- 우선 반드시 지나야 하는 두 정점 사이의 최소 거리를 구한다. (다익스트라)
    - 그리고 1번 정점과 v1, v2 / N번 정점과 v1, v2 사이의 거리를 구한 뒤 더 짧은 거리를 선택한다.

2. 시간 복잡도
- O(3 * ElgV) = 5 * 200000 * lg(800) =~ 2,903,089   -> 가능

3. 변수
- 정점의 개수, 간선의 개수 : int
- 힙 : (비용, 노드번호)
- 거리배열 : int[]
- 인접 간선 리스트 : (비용, 노드번호)[]
"""
import sys
import heapq
INF = sys.maxsize

input = sys.stdin.readline

N, E = map(int, input().split())
edge = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    edge[a].append([c, b])
    edge[b].append([c, a])

v1, v2 = map(int, input().split())


def min_dist(start_node, end_node):
    heap = [[0, start_node]]
    dist = [INF] * (N + 1)
    dist[start_node] = 0

    while heap:
        w, v = heapq.heappop(heap)
        if w != dist[v]: continue
        for nw, nv in edge[v]:
            if dist[nv] > dist[v] + nw:
                dist[nv] = dist[v] + nw
                heapq.heappush(heap, [dist[nv], nv])

    return dist[end_node]

dist_v1_to_v2 = min_dist(v1, v2)
dist_1_to_v1 = min_dist(1, v1)
dist_1_to_v2 = min_dist(1, v2)
dist_v1_to_N = min_dist(v1, N)
dist_v2_to_N = min_dist(v2, N)

total_dist = dist_v1_to_v2 + min(dist_1_to_v1 + dist_v2_to_N, dist_1_to_v2 + dist_v1_to_N)

print(total_dist if total_dist < INF else -1)