N = int(input())
M = int(input())

graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


cnt = 0
def dfs(V):
    visited[V] = True
    for i in range(2, N + 1):
        if not visited[i] and graph[V][i] == 1:
            dfs(i)
            global cnt
            cnt += 1

dfs(1)
print(cnt)