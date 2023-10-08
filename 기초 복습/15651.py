"""
1. 아이디어
- 중복을 허용하는 백트래킹

2. 시간 복잡도
- O(N^N) : 7 ** 7 =~ 800000     -> 가능

3. 변수
- N, M : int
- 결과 수열 : int[]
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, M = map(int, input().split())

sequence = []

def backtracking(num):
    if num == M:
        print(' '.join(map(str, sequence)))
        return
    else:
        for i in range(1, N + 1):
            sequence.append(i)
            backtracking(num + 1)
            sequence.pop()

backtracking(0)