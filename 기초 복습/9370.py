"""
1. 아이디어
- 출발지가 정해져 있고 최단거리로 이동한다고 하였으므로 다익스트라를 이용해야한다.

2. 시간 복잡도
- O(mlgm * T) = 50000 * lg(50000) * 100 ~= 20,000,000       -> 가능

3. 변수
- n, m, t : int
- s, g, h : int
- edge : int[][][]
- 목적지 후보 : int[]
- 다음 경로 저장 : heap
- 최단 경로 배열 : int[]
"""
import sys
import heapq
INF = sys.maxsize

input = sys.stdin.readline

T = int(input())


def find_min_dist(edge, start_node, end_node):
    dist = [INF] * (n + 1)
    dist[start_node] = 0
    heap = [[0, start_node]]

    while heap:
        w, v = heapq.heappop(heap)
        if w != dist[v]: continue
        for nw, nv in edge[v]:
            if dist[nv] > dist[v] + nw:
                dist[nv] = dist[v] + nw
                heapq.heappush(heap, [dist[nv], nv])

    return dist[end_node]


for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    edge = [[] for _ in range(n + 1)]
    g_h_dist = 0
    for _ in range(m):
        a, b, d = map(int, input().split())
        edge[a].append([d, b])
        edge[b].append([d, a])
        if (a == g and b == h) or (a == h and b == g):
            g_h_dist = d

    candidate_destination = []
    for _ in range(t):
        candidate_destination.append(int(input()))

    selected_destination = []
    for destination in candidate_destination:
        min_dist_through_g_h = min(find_min_dist(edge, s, g) + g_h_dist + find_min_dist(edge, h, destination),
                                   find_min_dist(edge, s, h) + g_h_dist + find_min_dist(edge, g, destination))

        min_dist = find_min_dist(edge, s, destination)

        if min_dist == min_dist_through_g_h:
            selected_destination.append(destination)

    selected_destination.sort()

    print(' '.join(map(str, selected_destination)))
