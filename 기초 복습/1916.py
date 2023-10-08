"""
1. 아이디어
- A번째 도시에서 B번째 도시까지 가는데 드는 최소비용 : 다익스트라

2. 시간복잡도
- O(ElgV) : 100000 * lg(1000) = 300,000     -> 가능

3. 변수
- N, M: int
- 버스 노선 정보 (인접 간선 리스트) : (버스 비용, 도착지 도시 번호)[]
- 출발점, 도착점 도시번호 : int
- 거리 배열 : int[]
"""
import sys
import heapq
sys.setrecursionlimit(10 ** 6)
INF = sys.maxsize

input = sys.stdin.readline

N = int(input())
M = int(input())

bus_info = [[] for _ in range(N + 1)]
for _ in range(M):
    start_city_node, arrival_city_node, cost = map(int, input().split())
    bus_info[start_city_node].append([cost, arrival_city_node])

start_city, arrival_city = map(int, input().split())

bus_cost = [INF] * (N + 1)
heap = [[0, start_city]]
bus_cost[start_city] = 0

while heap:
    w, v = heapq.heappop(heap)
    if w != bus_cost[v]: continue
    for nw, nv in bus_info[v]:
        if bus_cost[nv] > bus_cost[v] + nw:
            bus_cost[nv] = bus_cost[v] + nw
            heapq.heappush(heap, [bus_cost[nv], nv])

print(bus_cost[arrival_city])