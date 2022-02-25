import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

miro = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        if x == N-1 and y == M-1:
            break

        if y+1 < M and miro[x][y+1] == 1:
            queue.append([x, y+1])
            miro[x][y+1] = miro[x][y] + 1
        if x+1 < N and miro[x+1][y] == 1:
            queue.append([x+1, y])
            miro[x+1][y] = miro[x][y] + 1
        if y-1 > 0 and miro[x][y-1] == 1:
            queue.append([x, y-1])
            miro[x][y-1] = miro[x][y] + 1
        if x-1 > 0 and miro[x-1][y] == 1:
            queue.append([x-1, y])
            miro[x-1][y] = miro[x][y] + 1

    return miro[N-1][M-1]



print(bfs(0, 0))