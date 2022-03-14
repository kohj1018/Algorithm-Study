"""
1. 아이디어
브루트포스로 다 돌려본다. N이 최대 50이므로 가능하다.
한 위치에서 상하좌우와 바꿀 수 있지만 겹치므로 아래와 오른쪽만 계속해서 바꿔주면 된다.
바꿔준 뒤, 전체 보드에서 먹을 수 있는 사탕의 최대 개수를 구한 뒤 다시 원상복구 해주고
다음 걸로 넘어가 바꿔주고 확인하고를 반복하면 된다.

2. 시간복잡도
- O(N^4) : 50 ** 4 = 6250000 < 2억   -> 가능

3. 자료구조
N: int;
board: str[][];
maxCnt: int;
"""
import sys

input = sys.stdin.readline

N = int(input())
board = [list(input()) for _ in range(N)]
maxCnt = 0


def check():
    global maxCnt
    for i in range(N):
        cnt = 1     # 행을 검사
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1

        cnt = 1     # 열을 검사
        for j in range(1, N):
            if board[j][i] == board[j-1][i]:
                cnt += 1
                maxCnt = max(cnt, maxCnt)
            else:
                cnt = 1


for i in range(N):
    for j in range(N):
        # 오른쪽과 바꿈
        if j+1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            check()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        # 아래쪽과 바꿈
        if i+1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            check()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]


print(maxCnt)