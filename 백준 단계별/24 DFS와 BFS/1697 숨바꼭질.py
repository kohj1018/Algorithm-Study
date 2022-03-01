from collections import deque

N, K = map(int, input().split())
limit = 10 ** 5             # 시간초과 안나게 수 제한
dist = [0] * (limit + 1)    # 이동하는 거리를 알기 위한 리스트


def bfs(N, K):
    queue = deque()
    queue.append(N)
    while queue:
        N = queue.popleft()
        if N == K:
            print(dist[N])
            break
        for nN in (N - 1, N + 1, N * 2):
            if 0 <= nN <= limit and not dist[nN]:
                dist[nN] = dist[N] + 1
                queue.append(nN)

        # 아래는 위 for문과 같은 건데 밑으로 하면 틀렸다고 나옴.. 왜그런걸까
        # if limit >= 2 * N and dist[2 * N] == 0:
        #     queue.append(2 * N)
        #     dist[2 * N] = dist[N] + 1
        #
        # if limit >= N + 1 and dist[N + 1] == 0:
        #     queue.append(N + 1)
        #     dist[N + 1] = dist[N] + 1
        #
        # if 0 <= N - 1 and dist[N - 1] == 0:
        #     queue.append(N - 1)
        #     dist[N - 1] = dist[N] + 1


bfs(N, K)