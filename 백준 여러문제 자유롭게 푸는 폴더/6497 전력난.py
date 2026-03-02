import sys

input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break


    road_infos = [list(map(int, input().split())) for _ in range(n)]
    road_infos.sort(key=lambda x: x[2])

    parent = [i for i in range(m + 1)]

    total_cost = 0
    road_cnt = 0

    for x, y, z in road_infos:
        if find_parent(x) != find_parent(y):

            union_parent(x, y)
            total_cost += z
            road_cnt += 1

            if road_cnt == m - 1:
                break

    print( sum(x[2] for x in road_infos) - total_cost )

