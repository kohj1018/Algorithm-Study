"""
1. 아이디어
- 가장 적은 종류의 비행기 : BFS 탐색

2. 시간 복잡도
- BFS : O(V+E)
- V : 1000
- E : 10000
- T * (V+E) : 100 * (1000 + 10000) = 1,100,000  -> 가능

3. 변수
- 연결된 비행기 노선 : int[][]
- 방문 여부 : bool[]
- 비행기 이용 종류 수 : int
"""
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    graph = [[0] * (N + 1) for _ in range(N + 1)]
    visit = [False] * (N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    q = deque()
    q.append(1)
    visit[1] = True
    rs = -1

    while q:
        v = q.popleft()
        rs += 1
        for nv in range(1, N + 1):
            if not visit[nv] and graph[v][nv] == 1:
                q.append(nv)
                visit[nv] = True

    print(rs)
