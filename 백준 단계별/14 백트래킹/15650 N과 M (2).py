"""
1. 아이디어
백트래킹 함수 만들고 if문에는 길이 될때 return시키고
백트래킹 함수 파라매터 num이 depth를 나타내게
이때 밑에 for문 돌릴 때 for문 시작을 num으로하기
visited 리스트는 필요없을 듯

2. 시간복잡도
- 중복이 불가능한 경우 : O(N!)   (N = 10까지 가능) -> 가능

3. 자료구조
N, M: int;
result: int[];
"""
import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N, M = map(int, input().split())

result = []

def backTracking(v):
    result.append(v)
    if len(result)-1 == M:
        print(' '.join(map(str, result[1:])))
        return
    for i in range(v+1, N+1):
        backTracking(i)
        result.pop()


backTracking(0)