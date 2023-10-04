"""
1. 아이디어
MST를 이용해 그래프의 모든 정점을 연결하는 부분 그래프 중 가중치 합이 최소인 트리를 찾는다.
- 간선을 인접리스트에 집어넣기
- 힙에 시작점 넣기
- 힙이 빌 때까지 다음의 작업을 반복
    - 힙의 최소값을 꺼내서 해당 노드 방문 안했다면,
        - 방문표시, 해당 비용 추가, 연결된 간선들 힙에 넣어주기

2. 시간복잡도
- MST : O(ElgE)

3. 자료구조
- 간선 저장 되는 인접리스트 : (무게, 노드번호)
- 힙 : (무게, 노드번호)
- 방문 여부 : bool[]
- MST 결과값 : int
"""
import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

edge = [[] for _ in range(V + 1)]
visit = [False] * (V + 1)

for _ in range(E):
    A, B, C = map(int, input().split())
    edge[A].append([C, B])
    edge[B].append([C, A])

heap = [[0, 1]]
rs = 0

while heap:
    w, next_node = heapq.heappop(heap)
    if not visit[next_node]:
        visit[next_node] = True
        rs += w
        for next_edge in edge[next_node]:
            if not visit[next_edge[1]]:
                heapq.heappush(heap, next_edge)

print(rs)