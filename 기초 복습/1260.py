"""
1. 아이디어
DFS, BFS

2. 시간 복잡도
BFS, DFS -> O(V+E)
V : 1000
E : 10000
O(V+E) : 11000     -> 가능

3. 자료구조
graph: int[][]
방문 여부: bool[]
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
dfs_visit = [False] * (N + 1)
bfs_visit = [False] * (N + 1)

for _ in range(M):
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

dfs_result = []
bfs_result = []

def dfs(pre_v):
    dfs_result.append(pre_v)
    dfs_visit[pre_v] = True
    for new_v in range(1, N + 1):
        if graph[pre_v][new_v] == 1 and dfs_visit[new_v] == False:
            dfs(new_v)


def bfs():
    q = deque()
    q.append(V)
    bfs_visit[V] = True
    while q:
        pre_v = q.popleft()
        bfs_result.append(pre_v)
        for new_v in range(1, N + 1):
            if graph[pre_v][new_v] == 1 and bfs_visit[new_v] == False:
                bfs_visit[new_v] = True
                q.append(new_v)

dfs(V)
bfs()

print(' '.join(map(str, dfs_result)))
print(' '.join(map(str, bfs_result)))