import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
before_cnt = [0] * (N + 1)  # in_degree가 표준 명명이라고 함.
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    before_cnt[B] += 1

# first_nodes = []
# for idx, cnt in enumerate(before_cnt):
#     if idx == 0:
#         continue
#     if cnt == 0:
#         first_nodes.append(idx)

q = deque([i for i in range(1, N + 1) if before_cnt[i] == 0])
result = []
while q:
    current_node = q.popleft()
    result.append(current_node)
    for next_node in graph[current_node]:
        before_cnt[next_node] -= 1
        if before_cnt[next_node] == 0:
            q.append(next_node)

print(*result)
