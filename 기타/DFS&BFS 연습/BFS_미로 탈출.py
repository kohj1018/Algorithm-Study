from collections import deque


def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[N - 1][M - 1]


N, M = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))


# 다른 풀이
# import sys
# from collections import deque
#
# N, M = map(int, sys.stdin.readline().rstrip().split())
#
# miro = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     while queue:
#         x, y = queue.popleft()
#
#         if x == N-1 and y == M-1:
#             break
#
#         if y+1 < M and miro[x][y+1] == 1:
#             queue.append([x, y+1])
#             miro[x][y+1] = miro[x][y] + 1
#         if x+1 < N and miro[x+1][y] == 1:
#             queue.append([x+1, y])
#             miro[x+1][y] = miro[x][y] + 1
#         if y-1 > 0 and miro[x][y-1] == 1:
#             queue.append([x, y-1])
#             miro[x][y-1] = miro[x][y] + 1
#         if x-1 > 0 and miro[x-1][y] == 1:
#             queue.append([x-1, y])
#             miro[x-1][y] = miro[x][y] + 1
#
#     return miro[N-1][M-1]
#
#
# print(bfs(0, 0))