"""
1. 아이디어
- 특정 위치에 퀸을 놓는 것이 가능한지 여부를 판단하는 2차원 배열을 활용해 백트래킹

2. 시간복잡도
- 중복이 아닌 경우 : O(N!) : 15! = 1,307,674,368,000       ->

3. 변수
- N : int
- 가능 여부 : bool[][]
- 경우의 수 : int
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N = int(input())

available = [[True] * (N + 1) for _ in range(N + 1)]

caseCnt = 0

def backtracking(depth):
    print("-----------depth {}-----------".format(depth))
    print(available[depth])
    if depth == N + 1:
        global caseCnt
        caseCnt += 1
        return
    else:
        for i in range(1, N + 1):
            if available[depth][i]:
                for new_depth in range(depth + 1, N + 1):
                    available[new_depth][i] = False
                    if i + (new_depth - depth) < N + 1:
                        available[new_depth][i + (new_depth - depth)] = False
                    if i - (new_depth - depth) > 0:
                        available[new_depth][i - (new_depth - depth)] = False
                backtracking(depth + 1)
                for new_depth in range(depth + 1, N + 1):
                    available[new_depth][i] = True
                    if i + (new_depth - depth) < N + 1:
                        available[new_depth][i + (new_depth - depth)] = True
                    if i - (new_depth - depth) > 0:
                        available[new_depth][i - (new_depth - depth)] = True


backtracking(1)
print(caseCnt)