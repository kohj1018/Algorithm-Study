# <다익스트라 풀이>

import sys
import heapq

input = sys.stdin.readline

INF = float('inf')

N, K = map(int, input().split())

def dijkstra():
    dist = [INF] * 100001

    pq = []
    heapq.heappush(pq, (0, N))
    dist[N] = 0

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if dist[current_node] < current_dist:
            continue

        if current_node == K:
            return current_dist

        for weight, next_node in [(0, 2 * current_node), (1, current_node - 1), (1, current_node + 1)]:
            if 0 <= next_node <= 100000:
                next_dist = current_dist + weight

                if next_dist < dist[next_node]:
                    dist[next_node] = next_dist
                    heapq.heappush(pq, (next_dist, next_node))

    return dist[K]

print(dijkstra())




# <0-1 BFS 풀이>
#
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# N, K = map(int, input().split())
#
# dist = [-1] * 100001
#
# def zero_one_bfs():
#     if N == K:
#         return 0
#
#     q = deque([N])
#     dist[N] = 0
#
#     while q:
#         v = q.popleft()
#         for next_v in [v * 2, v - 1, v + 1]:
#             if next_v == K:
#                 if next_v == v * 2:
#                     return dist[v]
#                 else:
#                     return dist[v] + 1
#             if 0 <= next_v <= 100000:
#                 if dist[next_v] == -1:
#                     if next_v == v * 2:
#                         q.appendleft(next_v)
#                         dist[next_v] = dist[v]
#                     else:
#                         q.append(next_v)
#                         dist[next_v] = dist[v] + 1
#
# print(zero_one_bfs())