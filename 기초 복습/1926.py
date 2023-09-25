"""
1. 아이디어
이중 for문 돌면서 값이 1 + 방문 X 이면 BFS

2. 시간복잡도
BFS -> O(V+E)
V : n * m = 500 * 500 = 250,000
E : 4 * n * m = 4 * 500 * 500 = 1,000,000
O(V+E) : 1,250,000 < 2억     -> 가능

3. 자료구조
도화지 지도 : int[][]
방문 여부 : bool[][]
Queue(BFS)
"""
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(y, x):
    area = 1
    q = deque()
    q.append((y, x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if paper[ny][nx] == 1 and visit[ny][nx] is False:
                    visit[ny][nx] = True
                    area += 1
                    q.append((ny, nx))

    return area


cnt = 0
maxArea = 0
for j in range(n):
    for i in range(m):
        if paper[j][i] == 1 and visit[j][i] is False:
            cnt += 1
            visit[j][i] = True
            maxArea = max(maxArea, bfs(j, i))

print(cnt)
print(maxArea)
