import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().rstrip().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
DFS_visited = [False] * (N + 1)
BFS_visited = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x][y] = 1
    graph[y][x] = 1



def dfs(V):
    DFS_visited[V] = True
    print(V, end=' ')
    for i in range(1, N + 1):
        if not DFS_visited[i] and graph[V][i] == 1:
            dfs(i)



def bfs(V):
    BFS_visited[V] = True
    queue = deque()
    queue.append(V)
    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in range(1, N + 1):
            if not BFS_visited[i] and graph[V][i] == 1:
                queue.append(i)
                BFS_visited[i] = True



dfs(V)
print()
bfs(V)