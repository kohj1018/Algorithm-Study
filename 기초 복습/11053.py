"""
1. 아이디어
- DP
- 수열의 길이를 1부터 N까지 증가시켜가며 각각의 최대 길이 수열 값을 저장한다.

2. 시간 복잡도
- O(N^2) : 1,000,000       -> 가능

3. 변수
- N : int
- A : int[]
- longest_length : int[]
"""
import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

longest_length = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            longest_length[i] = max(longest_length[i], longest_length[j] + 1)

print(max(longest_length))