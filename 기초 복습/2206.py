# """
# 1. 아이디어
# - 백트래킹으로 탐색하며 벽을 뚫을 때와 안뚫을 떄를 구분하여 전체 가지수를 탐색한다.
#
# 2. 시간 복잡도
# - O(N * M) : 1000 * 1000 = 1,000,000     -> 가능
#
# 3. 변수
# - N, M : int
# - map : int[][]
# - visit : bool[][]
# """
# import sys
# sys.setrecursionlimit(10 ** 6)
# INF = sys.maxsize
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# map = [list(map(int, input().rstrip())) for _ in range(N)]
# visit = [[False] * M for _ in range(N)]
#
# dy = [0, -1, 0, 1]
# dx = [-1, 0, 1, 0]
#
# min_dist = INF
#
#
# def backtracking(x, y, dist, break_the_wall):
#     if x == N - 1 and y == M - 1:
#         global min_dist
#         if dist < min_dist:
#             min_dist = dist
#         return
#     else:
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < M:
#                 if not visit[nx][ny]:
#                     if map[nx][ny] == 0:
#                         visit[nx][ny] = True
#                         backtracking(nx, ny, dist + 1, break_the_wall)
#                         visit[nx][ny] = False
#                     elif map[nx][ny] == 1 and break_the_wall == False:
#                         visit[nx][ny] = True
#                         backtracking(nx, ny, dist + 1, True)
#                         visit[nx][ny] = False
#
#
# backtracking(0, 0, 1, False)
#
# print(min_dist if min_dist < INF - 1 else -1)

"""
1. 아이디어
- 3차원의 방문 여부 배열을 만들고 z축에서 0이면 아직 벽을 부수지 않은 경우, 1이면 벽을 부순 경우로 생각하여 BFS로 탐색한다.

2. 시간 복잡도
- O(2NM + 8NM) : 10 * 1000 * 1000 = 10,000,000     -> 가능

3. 변수
- N, M : int
- map : int[][]
- visit : int[][][]
"""
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

map = [list(map(int, input().rstrip())) for _ in range(N)]
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]

q = deque()
q.append([0, 0, 0])
visit[0][0][0] = 1

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

while q:
    x, y, z = q.popleft()
    if x == N - 1 and y == M - 1:
        print(visit[x][y][z])
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            # 이동할 곳이 벽이고 벽 파괴 기회를 사용 하지 않은 경우
            if map[nx][ny] == 1 and z == 0:
                visit[nx][ny][1] = visit[x][y][z] + 1
                q.append([nx, ny, 1])
            # 이동할 곳이 벽이 아니고 아직 방문 하지 않은 경우
            elif map[nx][ny] == 0 and not visit[nx][ny][z]:
                visit[nx][ny][z] = visit[x][y][z] + 1
                q.append([nx, ny, z])
else:
    print(-1)