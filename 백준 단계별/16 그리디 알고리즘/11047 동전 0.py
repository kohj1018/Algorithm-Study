"""
1. 아이디어
동전 세트에 따라 GA가 되지 않을 수 있지만 GA로 풀 수 있게 해준다고 하니
가장 큰 화폐 단위로 나누고 그 몫은 카운트에 포함시키고 나머지를 가지고 계속 계산하는 방식으로 가면 된다.

2. 시간복잡도

3. 자료구조
N, K: int;
value: int[];
cnt: int;
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
value = []
for _ in range(N):
    value.append(int(input()))

cnt = 0
for i in reversed(range(N)):
    cnt += K // value[i]
    K %= value[i]
print(cnt)
# divNum = 0
# while 1:
#     if K == 0:
#         print(cnt)
#         break
#     for i in range(N):
#         if i == N-1 and value[i] <= K:
#             divNum = value[i]
#         if value[i] > K:
#             divNum = value[i-1]
#             break
#     cnt += K // divNum
#     K %= divNum