import sys
import heapq

input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    root_a = find_parent(a)
    root_b = find_parent(b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

while True:
    m, n = map(int, input().split())

    if m == 0 and n == 0:
        break

    heap = []
    parent = [i for i in range(m)]
    max_budget = 0
    min_budget = 0

    for _ in range(n):
        x, y, z = map(int, input().split())
        heapq.heappush(heap, [z, x, y])
        max_budget += z

    while heap:
        cur_z, cur_x, cur_y = heapq.heappop(heap)
        if find_parent(cur_x) != find_parent(cur_y):
            union_parent(cur_x, cur_y)
            min_budget += cur_z

    print(max_budget - min_budget)