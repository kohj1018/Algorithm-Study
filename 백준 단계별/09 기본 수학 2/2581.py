M = int(input())
N = int(input())

primeNum = []
for i in range(M, N+1):
    if i >= 2:
        primeNum.append(i)
        for j in range(2, i):
            if i % j == 0:
                primeNum.pop()
                break

if len(primeNum) == 0:
    print(-1)
else:
    print(sum(primeNum))
    print(primeNum[0])
