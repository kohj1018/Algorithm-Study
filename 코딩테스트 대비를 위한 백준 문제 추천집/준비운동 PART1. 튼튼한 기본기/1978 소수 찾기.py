N = int(input())
numList = list(map(int, input().split()))

cnt = 0
for num in numList:
    fetch = False
    if num == 1:
        fetch = True
    for divider in range(2, num):
        if num % divider == 0:
            fetch = True
            break

    if not fetch:
        cnt += 1

print(cnt)