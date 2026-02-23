import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

dist = [-1] * 100001

def zero_one_bfs():
    if N == K:
        return 0

    q = deque([N])
    dist[N] = 0

    while q:
        v = q.popleft()
        for next_v in [v * 2, v - 1, v + 1]:
            if next_v == K:
                if next_v == v * 2:
                    return dist[v]
                else:
                    return dist[v] + 1
            if 0 <= next_v <= 100000:
                if dist[next_v] == -1:
                    if next_v == v * 2:
                        q.appendleft(next_v)
                        dist[next_v] = dist[v]
                    else:
                        q.append(next_v)
                        dist[next_v] = dist[v] + 1

print(zero_one_bfs())