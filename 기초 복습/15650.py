"""
1. 아이디어
중복없이 M개, 오름차순 -> 백트래킹

2. 시간복잡도
- 중복이 불가능한 경우 : O(N!) = 8! =~ 40000 -> 가능

3. 변수
- N, M : int
- 결과 배열 : int[]
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, M = map(int, input().split())

sequence = []

def backtracking(num, max_num):
    if num == M:
        print(' '.join(map(str, sequence)))
        return
    else:
        for i in range(max_num + 1, N + 1):
            sequence.append(i)
            backtracking(num + 1, i)
            sequence.pop()


backtracking(0, 0)