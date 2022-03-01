"""
1. 아이디어
for문으로 graph의 전 부분을 돌면서
1인 부분에 dfs로 들어가고 방문한 곳은 0으로 바꾸고 한번 dfs 순회할 때 cnt 증가시키기

2. 시간복잡도

3. 자료구조
M, N, K: int;
graph: int[][];
x, y: int;
dx, dy: int[];
"""
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(x, y):
    graph[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                dfs(nx, ny)


T = int(input())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                cnt += 1
                dfs(j, i)

    print(cnt)