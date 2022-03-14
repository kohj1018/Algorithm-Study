"""
1. 아이디어
통로를 2차원 배열로 표현하고 음식물 쓰레기의 좌표를 받아 1로 표현한다. (나머지 부분은 0으로)
그리고 이중 for문 돌리면서 dfs 탐색하고 그중 가장 큰거 선택

2. 시간복잡도
- O(NM)

3. 자료구조
N, M, K: int;
hallWay: int[][];
curCnt: int;
maxTrashCnt: int;
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, M, K = map(int, input().split())
hallWay = [[0] * (M+1) for _ in range(N+1)]
for _ in range(K):
    r, c = map(int, input().split())
    hallWay[r][c] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    hallWay[x][y] = 0
    global curCnt
    curCnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<nx<=N and 0<ny<=M and hallWay[nx][ny] == 1:
            hallWay[nx][ny] = 0
            dfs(nx, ny)


maxTrashCnt = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if hallWay[i][j] == 1:
            curCnt = 0
            dfs(i, j)
            maxTrashCnt = max(curCnt, maxTrashCnt)

print(maxTrashCnt)