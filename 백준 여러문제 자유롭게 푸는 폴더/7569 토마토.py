import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

tomatoes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

first_nodes = []
is_all_mature = True
for m in range(M):
    for n in range(N):
        for h in range(H):
            if tomatoes[h][n][m] == 1:
                first_nodes.append([m, n, h])
            if tomatoes[h][n][m] == 0:
                is_all_mature = False

if is_all_mature:
    print(0)
else:
    result_day = 0

    q = deque(first_nodes)

    while q:
        m, n, h = q.popleft()
        for next_m, next_n, next_h in [[m + 1, n, h], [m, n + 1, h], [m - 1, n, h], [m, n - 1, h], [m, n, h - 1], [m, n, h + 1]]:
            if 0 <= next_m < M and 0 <= next_n < N and 0 <= next_h < H:
                if tomatoes[next_h][next_n][next_m] == 0:
                    tomatoes[next_h][next_n][next_m] = tomatoes[h][n][m] + 1
                    result_day = max(result_day, tomatoes[next_h][next_n][next_m])
                    q.append([next_m, next_n, next_h])

    is_all_mature = True
    for m in range(M):
        for n in range(N):
            for h in range(H):
                if tomatoes[h][n][m] == 0:
                    is_all_mature = False

    if is_all_mature:
        print(result_day - 1)
    else:
        print(-1)