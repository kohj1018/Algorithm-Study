N, K = map(int, input().split())

cnt = 0
fetch = False
for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
        if cnt == K:
            fetch = True
            print(i)

if not fetch:
    print(0)