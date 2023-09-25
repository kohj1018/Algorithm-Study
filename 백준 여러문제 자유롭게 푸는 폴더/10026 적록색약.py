import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

picture = [list(input().rstrip()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]

def dfs(y, x, char):
    visit[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if visit[ny][nx] == 0 and picture[ny][nx] == char:
                visit[ny][nx] = 1
                dfs(ny, nx, char)


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
normal_cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            normal_cnt += 1
            dfs(i, j, picture[i][j])


visit = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'
abnormal_cnt = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            abnormal_cnt += 1
            dfs(i, j, picture[i][j])

print(normal_cnt, abnormal_cnt)