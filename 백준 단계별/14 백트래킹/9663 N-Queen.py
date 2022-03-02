"""
1. 아이디어
첫번째 행부터 내려가면서 놓는다.
행 내려가는걸 트리 depth 내려가는 것으로 생각.
두다가 놓을 수 없으면 뒤로 백트래킹해서 다시 찾기

2. 시간복잡도
- 중복불가능 : O(n!) (n = 15의 경우 1조 3천억)
- 문제 시간 제한 10초 : 10 * 2억 -> 20억

3. 자료구조
N: int;
cnt: int;
visited 리스트들: bool[][];
"""
# 이 문제 pypy3로 안하면 시간초과뜸...
import sys
sys.setrecursionlimit(10 ** 4)  # 10 ** 6으로 했더니 메모리 초과남

input = sys.stdin.readline

N = int(input())
col_visited = [False] * N               # 열 확인
diag_visited1 = [False] * (2 * N - 1)   # 대각선 확인
diag_visited2 = [False] * (2 * N - 1)   # 대각선 확인 2


cnt = 0
def backTracking(x):
    if x == N:
        global cnt
        cnt += 1
        return
    for y in range(N):
        if not col_visited[y] and not diag_visited1[y - x + (N-1)] and not diag_visited2[x + y]:
            col_visited[y] = True
            diag_visited1[y - x + (N-1)] = True
            diag_visited2[x + y] = True
            backTracking(x + 1)
            col_visited[y] = False
            diag_visited1[y - x + (N-1)] = False
            diag_visited2[x + y] = False


backTracking(0)
print(cnt)