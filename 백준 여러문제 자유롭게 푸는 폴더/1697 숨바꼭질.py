import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
dist = [-1] * 100001

def bfs(start_node):
    if start_node == K:
        return 0

    q = deque([start_node])
    dist[start_node] = 0

    while q:
        v = q.popleft()
        for next_node in [v - 1, v + 1, v * 2]:
            if next_node == K:
                return dist[v] + 1
            if 0 <= next_node <= 100000:
                if dist[next_node] == -1:
                    q.append(next_node)
                    dist[next_node] = dist[v] + 1

print(bfs(N))