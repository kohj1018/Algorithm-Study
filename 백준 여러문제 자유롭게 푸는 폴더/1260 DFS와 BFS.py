import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

dfs_visited = [False] * (N + 1)
dfs_result = []
def dfs(v):
    dfs_visited[v] = True
    dfs_result.append(v)
    for i in range(1, N + 1):
        if not dfs_visited[i] and graph[v][i] == 1:
            dfs(i)

bfs_visited = [False] * (N + 1)
bfs_result = []
def bfs():
    q = deque([V])
    bfs_visited[V] = True

    while q:
        if len(bfs_result) == N:
            break

        v = q.popleft()
        bfs_result.append(v)
        for i in range(1, N + 1):
            if not bfs_visited[i] and graph[v][i] == 1:
                bfs_visited[i] = True
                q.append(i)

dfs(V)
print(*dfs_result)
bfs()
print(*bfs_result)