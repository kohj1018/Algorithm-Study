"""
1. 아이디어
- 음의 순환이 발생할 수 있기 때문에 다익스트라 알고리즘으로는 풀 수 없다.
    - 벨만 포드 알고리즘 활용

2. 시간 복잡도
- O(VE) : 500 * 6000 = 3,000,000        -> 가능

3. 변수
- N, M : int
- edges : int[][]
"""
import sys
INF = sys.maxsize

input = sys.stdin.readline

N, M = map(int, input().split())

edges = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append([A, B, C])

dist = [INF] * (N + 1)
dist[1] = 0

is_negative_cycle = False

for i in range(N):
    for edge in edges:
        cur_city, arr_city, time = edge
        if dist[cur_city] != INF and dist[arr_city] > dist[cur_city] + time:
            dist[arr_city] = dist[cur_city] + time
            if i == N - 1:
                is_negative_cycle = True
                break

if is_negative_cycle:
    print(-1)
else:
    print('\n'.join(map(lambda x: str(x) if x < INF - 1 else '-1', dist[2:])))
