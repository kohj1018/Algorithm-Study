"""
1. 아이디어
BFS로 최단 이동 횟수를 구한다.
나이트가 이동할 수 있는 방향은 총 8가지다.
이동 가능하다면 큐에 넣고 pop을 하면서 for문 돌려서 해당 위치에서 갈 수 있는 위치를 다시 찾는다.

2. 시간복잡도
- O(I^2) : 300 * 300 = 90000 < 2억   -> 가능

3. 자료구조
T: int;
I: int;
x, y: int;
a, b: int;
board: int[][];
"""
import sys
from collections import deque

input = sys.stdin.readline

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x, y, a, b):
    queue = deque()
    queue.append((x, y))
    while queue:
        popX, popY = queue.popleft()
        if popX == a and popY == b:
            print(board[a][b])
            break
        for i in range(8):
            nx = popX + dx[i]
            ny = popY + dy[i]
            if 0<=nx<I and 0<=ny<I and board[nx][ny] == 0:
                queue.append((nx, ny))
                board[nx][ny] = board[popX][popY] + 1


T = int(input())
for _ in range(T):
    I = int(input())
    board = [[0] * I for _ in range(I)]
    x, y = map(int, input().split())
    a, b = map(int, input().split())

    bfs(x, y, a, b)
