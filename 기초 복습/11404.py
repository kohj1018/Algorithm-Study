"""
1. 아이디어
- 어떤 도시에서 어떤 도시로 가는 모든 비용을 구해야하므로 플로이드 알고리즘을 이용한다.
    - 거리 비용 그래프를 만들고 INF로 초기화한다.
    - 입력받은 거리 비용을 입력한다.
    - 삼중 for문을 통해 Divide-and-Conquer 개념으로 도시를 하나씩 추가해가며 해당 도시를 거칠 때 비용이 줄어든다면 최소 거리비용을 기록한다.

2. 시간 복잡도
- O(n^3) : 1,000,000        -> 가능

3. 변수
- n, m : int
- cost : int[][]
"""
import sys
INF = sys.maxsize

input = sys.stdin.readline

n = int(input())
m = int(input())

cost = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    cost[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a][b] = min(cost[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if cost[i][j] > cost[i][k] + cost[k][j]:
                cost[i][j] = cost[i][k] + cost[k][j]

for l in range(1, n + 1):
    print(' '.join(map(lambda x: str(x) if x < INF else '0', cost[l][1:])))