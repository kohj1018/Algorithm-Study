import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())

given_micro = [[] for _ in range(Q)]
for i in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    for r in range(r1, r2):
        for c in range(c1, c2):
            given_micro[i].append([r, c])

micro = []
container = [[-1] * N for _ in range(N)]

for i in range(Q):

    # 1-1. 미생물 투입
    new_micro = given_micro[i]
    micro.append(new_micro)
    for r, c in new_micro:
        if container[r][c] != -1:
            micro[container[r][c]].remove([r, c])

        container[r][c] = i

    # 1-2. 무리가 둘 이상으로 나뉘어지면 배양 용기에서 사라짐
    visited = [[False] * N for _ in range(N)]
    visited_micro = [False] * N

    delete_candidates = []
    for r in range(r1, r2):
        for c in range(c1, c2):
            if not visited[r][c]:
                selected_micro_num = container[r][c]

                if visited_micro[selected_micro_num]:
                    delete_candidates.append(selected_micro_num)

                if selected_micro_num != -1:

                    visited_micro[selected_micro_num] = True

                    q = deque([[r, c]])
                    visited[r][c] = True

                    while q:
                        cur_r, cur_c = q.popleft()
                        for next_r, next_c in [[cur_r + 1, cur_c], [cur_r, cur_c + 1], [cur_r - 1, cur_c],
                                               [cur_r, cur_c - 1]]:
                            if not visited[next_r][next_c] and container[next_r][next_c] == selected_micro_num:
                                visited[next_r][next_c] = True
                                q.append([next_r, next_c])

    for idx in sorted[delete_candidates, reverse=True]:
        del micro[idx]

    # 2-1. 새 배양용기 마련
    container = [[-1] * N for _ in range(N)]

    micro.sort(key=len, reverse=True)
