"""
1. 아이디어
- 한 점에서 시작, 모든 거리 : 다익스트라
- 간선, 인접리스트 저장
- 거리배열 무한대 초기화
- 시작점 : 거리배열 0, 힙에 넣어주기
- 힙에서 빼면서 다음의 것들 수행
    - 최신 값인지 먼저 확인
    - 간선을 타고 간 비용이 더 작으면 갱신

2. 시간복잡도
- 다익스트라 : O(ElgV)
    - E : 3e5
    - V : 2e4, lgV ~= 20
    - ElgV = 6e6      -> 가능

3. 변수
- 힙 : (비용, 노드번호)
- 거리 배열 : 비용 : int[]
- 간선 저장, 인접리스트 : (비용, 노드번호)[]
"""
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())

edge = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    edge[u].append([w, v])

dist = [INF] * (V + 1)
heap = [[0, K]]
dist[K] = 0

while heap:
    w, v = heapq.heappop(heap)
    if w != dist[v]: continue
    for nw, nv in edge[v]:
        if dist[nv] > dist[v] + nw:
            dist[nv] = dist[v] + nw
            heapq.heappush(heap, [dist[nv], nv])

print('\n'.join(map(lambda x: 'INF' if x >= INF - 1 else str(x), dist[1:])))
