"""
1. 아이디어
# 연산자들 숫자만큼 리스트로 연산자를 담고 백트래킹으로 순회한다.
# 그리고 각각의 결과값을 구해 비교하여 최댓값과 최솟값을 구한다.


2. 시간복잡도
- O(N^2) : 100 * 100 < 2억   -> 가능

3. 자료구조
N: int;
A: int[];
operator: str[];
canUsedCnt: int[];
maxValue, minValue: int;
"""
# ↓ 새로운 풀이
import sys
sys.setrecursionlimit(10 ** 4)

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
operator = list(map(int, input().split()))

maxResult = -1000000000
minResult = 1000000000



def backTracking(curResult, idx):
    if idx == N:
        global maxResult, minResult
        maxResult = max(maxResult, curResult)
        minResult = min(minResult, curResult)
        return
    li = [curResult+A[idx], curResult-A[idx], curResult*A[idx], int(curResult/A[idx])]
    for i, nextResult in enumerate(li):
        if operator[i]:
            operator[i] -= 1
            backTracking(nextResult, idx+1)
            operator[i] += 1


backTracking(A[0], 1)
print(maxResult)
print(minResult)

# N = int(input())
# A = list(map(int, input().split()))
# canUsedCnt = list(map(int, input().split()))
#
# operatorList = []
# maxValue = -10000000000
# minValue = 10000000000
#
#
# def backTracking():
#     if len(operatorList) == N-1:
#         result = A[0]
#         for i in range(N-1):
#             if operatorList[i] == 0:
#                 result += A[i+1]
#             elif operatorList[i] == 1:
#                 result -= A[i+1]
#             elif operatorList[i] == 2:
#                 result *= A[i+1]
#             elif operatorList[i] == 3:
#                 result = int(result / A[i+1])
#         global maxValue
#         global minValue
#         if result > maxValue:
#             maxValue = result
#         if result < minValue:
#             minValue = result
#
#     for i in range(4):
#         if canUsedCnt[i] > 0:
#             operatorList.append(i)
#             canUsedCnt[i] -= 1
#             backTracking()
#             operatorList.pop()
#             canUsedCnt[i] += 1
#
#
# backTracking()
# print(maxValue)
# print(minValue)