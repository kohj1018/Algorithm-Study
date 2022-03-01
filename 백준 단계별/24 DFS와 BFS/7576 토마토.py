"""
1. 아이디어
bfs로 queue를 만들고 1인 지점부터 시작해서 queue에 넣고 pop하길 반복한다.
처음 시작할 때 1인 지점을 몽땅 queue에 넣어두고 시작한다.
처음 1인 곳이 여러곳일 수 있다.
그래서 queue에 있는걸 다 처리하게 해야한다. 따로 if문을 두고 break하지 않는다.
마지막에 이중포문 돌리면서 익지못한 토마토(0)가 있는지 확인 없다면 가장 큰 숫자 출력

2. 시간복잡도
- BFS : O(V + E)
- V : 1000 * 1000
- E : 4 * 1000 * 1000
- V + E : 5 * 1000 * 1000 = 5e6 (5백만)
- 이중포문 : O(NM)
- NM : 1000 * 1000
- 전체 시간복잡도 : O(6NM) = 6e6 (6백만)
- 2억보다 작으므로 가능!

3. 자료구조
M, N: int;
graph: int[][];
queue: (int, int)[];
maxDay: int;
"""
import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
# 초기 시작 좌표를 queue에 담기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))


def bfs():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


bfs()
fetch = False   # 혹시 0이 나온다면 이중포문을 탈출하기 위한 장치
maxDay = 0
for i in range(N):
    if fetch: break   # fetch가 True가 되면 0이 나왔다는 얘기이므로 break로 탈출
    for j in range(M):
        if graph[i][j] == 0:
            # fetch를 True로 바꾸고 break
            fetch = True
            maxDay = 0
            break
        if maxDay < graph[i][j]:
            # 탐색한 칸의 값(날짜 수)가 더 크다면 바꾸기
            maxDay = graph[i][j]

# 처음 칸이 1로 시작하므로 1을 빼줘야 함 (총 날짜 수 중 시작하는 날은 빼야하므로)
print(maxDay - 1)