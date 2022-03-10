"""
1. 아이디어
- 모두 다 : 현재 위치 청소
- 왼쪽 청소 X -> 왼쪽으로 감
- 왼쪽 청소 O -> 왼쪽 방향 돌리고 왼쪽 청소했는지 확인
- 네 방향 청소 O -> 첫 방향에서 오른쪽 방향으로 돌리고 뒤로 후진
- 아무 곳도 못감 -> 중지
graph 받고 바라보는 방향으로부터 왼쪽으로 for문 돌리면서 확인하고 이동
while문 무한루프 두고 검사해서 개수 찾기

2. 시간복잡도
- O(NM) : 2500 가능

3. 자료구조
N, M: int;
r, c, d: int;
graph: int[][];
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

graph[r][c] = 2
cnt = 1
while 1:
    fetch = False
    for i in range(1, 5):
        nd = (d-i+4) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        if 0<=nr<N and 0<=nc<M and graph[nr][nc] == 0:
                r = nr
                c = nc
                d = nd
                cnt += 1
                graph[r][c] = 2
                fetch = True
                break

    if not fetch:
        nr = r - dr[d]
        nc = c - dc[d]
        if 0<=nr<N and 0<=nc<M and graph[nr][nc] != 1:
            r = nr
            c = nc
        else:
            break


print(cnt)