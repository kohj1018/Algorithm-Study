def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

all_list = list(range(2,10001)) # 문제에서 주어진 범위
prime_list = []   # all_list의 원소들중 소수들만 모은 리스트

for ele in all_list:    # 주어진 범위 안의 소수들을 찾아서 저장해놓는다.
    if isPrime(ele):
        prime_list.append(ele)

T = int(input())
for _ in range(T):
    n = int(input())
    for idx, ele in enumerate(prime_list):
        if int(n/2) <= ele:
            midIdx = idx
            break

    for i in range(midIdx, n):
        finish = False
        for j in range(midIdx, -1, -1):
            if n == prime_list[i] + prime_list[j]:
                print(prime_list[j], prime_list[i], sep=' ')
                finish = True
                break
        if finish:
            break


# 더 짧은 풀이 ↓
# prime_list = [0 for i in range(10001)]
# prime_list[1] = 1
#
# for i in range(2, 98):
#     for j in range(i * 2, 10001, i):
#         prime_list[j] = 1
#
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     midIdx = n // 2
#     for k in range(midIdx, 1, -1):
#         if prime_list[n - k] == 0 and prime_list[k] == 0:
#             print(k, n - k)
#             break
