"""
1. 아이디어
백트래킹

2. 시간 복잡도
- BackTracking
- 중복이 가능한 경우 : O(N^N) -> N = 8 까지 가능
- 중복이 불가능한 경우 : O(N!) -> N = 10 까지 가능

3. 자료구조
방문여부 : bool[]
수열 : int[]
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, M = map(int, input().split())

sequence = []
visit = [False] * (N + 1)

def backtracking(num):
    if num == M:
        print(' '.join(map(str, sequence)))
        return
    for i in range(1, N + 1):
        if not visit[i]:
            visit[i] = True
            sequence.append(i)
            backtracking(num + 1)
            visit[i] = False
            sequence.pop()

backtracking(0)