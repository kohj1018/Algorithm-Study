"""
1. 아이디어
bfs를 사용해 탐색하고 1이 있는 다음칸으로 넘어갈 때 이전 칸의 숫자에 +1을 해서 다음칸 숫자를 넣는다.
그렇게 탐색하다가 (N, M)에 도착하면 graph[N][M]의 값을 출력

2. 시간복잡도
    O(N^2) ?

3. 자료구조
N, M: int;
graph: int[][];
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))


def bfs():
    queue = deque()
    queue.append((0, 0))
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == M-1:
            print(graph[N - 1][M - 1])
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


bfs()
