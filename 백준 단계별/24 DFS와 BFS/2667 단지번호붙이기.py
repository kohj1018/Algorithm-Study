N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(x, y):
    graph[x][y] = 0
    global houseCnt
    houseCnt += 1

    if N > x + 1 and graph[x+1][y] == 1:
        dfs(x+1, y)
    if N > y + 1 and graph[x][y+1] == 1:
        dfs(x, y+1)
    if 0 <= x - 1 and graph[x-1][y] == 1:
        dfs(x-1, y)
    if 0 <= y - 1 and graph[x][y-1] == 1:
        dfs(x, y-1)


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