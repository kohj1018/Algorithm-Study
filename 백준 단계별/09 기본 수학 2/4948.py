def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

### 시간초과 나서 추가한 부분 ###
all_list = list(range(2,246912)) # 문제에서 주어진 범위
prime_list=[]   # all_list의 원소들중 소수들만 모은 리스트

for ele in all_list:    # 주어진 범위 안의 소수들을 찾아서 저장해놓는다.
    if isPrime(ele):
        prime_list.append(ele)
############################

while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for k in prime_list:
        if n < k <= n*2:
            cnt += 1
    print(cnt)
