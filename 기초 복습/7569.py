"""
1. 아이디어
- 3차원의 그래프를 만든 뒤 BFS로 순회한다.

2. 시간 복잡도
- O(V + E) : 100 * 100 * 100 + 30000 ~= 1,000,000        -> 가능

3. 변수
- M, N, H : int
- box : int[][][]
- queue
"""
import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()

is_unripe_present = False

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                q.append([i, j, k])
            elif box[i][j][k] == 0:
                is_unripe_present = True


if is_unripe_present:
    dz = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]
    dx = [0, 0, -1, 1, 0, 0]

    max_day = 0

    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nz = dz[i] + z
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[z][y][x] + 1
                    max_day = max(max_day, box[z][y][x] + 1)
                    q.append([nz, ny, nx])

    is_unripe_present = False

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box[i][j][k] == 0:
                    is_unripe_present = True

    if is_unripe_present:
        print(-1)
    else:
        print(max_day - 1)

else:
    print(0)
