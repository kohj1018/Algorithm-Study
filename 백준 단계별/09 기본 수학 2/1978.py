N = int(input())
numList = list(map(int, input().split()))

cnt = N
for num in numList:
    if num < 2:
        cnt -= 1
    else:
        for i in range(2, num):
            if num % i == 0:
                cnt -= 1
                break
print(cnt)
