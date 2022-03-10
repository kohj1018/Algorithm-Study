N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    graph[x][y] = 0
    global houseCnt
    houseCnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 1:
            dfs(nx, ny)


cnt = 0
result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt += 1
            houseCnt = 0
            dfs(i, j)
            result.append(houseCnt)

print(cnt)
result.sort()
for resultItem in result:
    print(resultItem)