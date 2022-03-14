"""
1. 아이디어
이중 for문 돌려 방문안한 것에 대해서 dfs로 순회한다.
한 뭉텅이에 몇명있는지 구하고 그것의 제곱을 구해 위력의 합을 구한다.

2. 시간복잡도
- O(NM)

3. 자료구조
N, M: int;
battleGround: str[][];
totalOurArmyPower, totalEnemyPower: int;
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, M = map(int, input().split())
battleGround = [list(input().rstrip()) for _ in range(M)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
totalOurArmyPower = 0
totalEnemyPower = 0


def dfs(x, y, type):
    global cnt
    cnt += 1
    battleGround[x][y] = 'Check'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<M and 0<=ny<N:
            if battleGround[nx][ny] == type:
                battleGround[nx][ny] = 'Check'
                dfs(nx, ny, type)


for i in range(M):
    for j in range(N):
        if battleGround[i][j] == 'W':
            cnt = 0
            dfs(i, j, 'W')
            totalOurArmyPower += cnt ** 2
        if battleGround[i][j] == 'B':
            cnt = 0
            dfs(i, j, 'B')
            totalEnemyPower += cnt ** 2


print(totalOurArmyPower, totalEnemyPower)