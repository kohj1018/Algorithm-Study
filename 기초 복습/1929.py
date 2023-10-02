"""
1. 아이디어

"""

# ↓ 파이썬은 함수 내부에서 도는 코드가 더 빠르다고 함. 그래서 아래 코드는 시간초과가 발생
# import sys
#
# input = sys.stdin.readline
#
# M, N = map(int, input().split())
#
# for i in range(M, N + 1):
#     isPrimeNum = True
#     if i == 1:
#         isPrimeNum = False
#     else:
#         for j in range(2, int(i ** 0.5) + 1):
#             if i % j == 0:
#                 isPrimeNum = False
#
#     if isPrimeNum:
#         print(i)

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)