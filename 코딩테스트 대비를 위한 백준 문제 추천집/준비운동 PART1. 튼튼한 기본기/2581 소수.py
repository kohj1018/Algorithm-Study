M = int(input())
N = int(input())

decimal = []
for num in range(M, N+1):
    fetch = False
    if num == 1:
        continue
    for divider in range(2, num):
        if num % divider == 0:
            fetch = True
            break

    if not fetch:
        decimal.append(num)

if decimal:
    print(sum(decimal))
    print(decimal[0])
else:
    print(-1)