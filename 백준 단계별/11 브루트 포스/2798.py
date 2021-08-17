N, M = map(int, input().split())
cards = list(map(int, input().split()))

maxSco = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sumSco = cards[i] + cards[j] + cards[k]
            if maxSco < sumSco <= M:
                maxSco = sumSco
print(maxSco)
