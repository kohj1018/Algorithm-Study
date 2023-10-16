"""
1. 아이디어
- 백트래킹
- 1차원 배열의 인덱스를 체스판의 행으로, 값을 열로 생각하면 1차원 배열만으로 표현할 수 있다.
    - promising function은 배열안의 값이 같지 않고 (같은 열 X)
    - 값끼리의 차이와 인덱스끼리의 차이가 같지 않은 경우를 걸러낸다. (대각선 X)

2. 시간복잡도
-

3. 변수
- N : int
- 체스 말 놓는 포지션 : int[]
- 경우의 수 : int
"""
import sys

input = sys.stdin.readline

N = int(input())

ps = []
cnt = 0


def can_be_placed(idx, value):
    for past_idx, past_value in enumerate(ps):
        if value == past_value:
            return False
        if abs(idx - past_idx) == abs(value - past_value):
            return False

    return True


def backtracking(idx):
    if idx == N:
        global cnt
        cnt += 1
        return
    else:
        for i in range(N):
            if can_be_placed(idx, i):
                ps.append(i)
                backtracking(idx + 1)
                ps.pop()


backtracking(0)
print(cnt)
