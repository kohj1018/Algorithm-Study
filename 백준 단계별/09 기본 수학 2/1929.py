# 이거 틀렸다고 함.
# (일반적인 소수 판별 알고리즘으로는 시간초과)
# 아래쪽 코드인 에라토스테네스의 체라는 소수 판별 알고리즘을 이용해야한다.
# M, N = map(int, input().split())
#
# for i in range(M, N+1):
#     primeNum = True
#     if i == 1:
#         primeNum = False
#     else:
#         for j in range(2, i):
#             if i % j == 0:
#                 primeNum = False
#                 break
#     if primeNum:
#         print(i)

# 에라토스테네스의 체 소수 판별 알고리즘 ↓
# 인자로 들어온 수의 제곱근까지만 확인하여 소수인지 아닌지를 검증하는 함수
def isPrime(num):
    if num == 1:
        return False
    else:
        for n in range(2, int(num**0.5)+1):
            if num % n == 0:
                return False
        return True

M, N = map(int, input().split())

for i in range(M, N+1):
    if isPrime(i):
        print(i)
