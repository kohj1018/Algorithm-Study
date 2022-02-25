N, M, K = input().split()

limitTime = int(N) / 100 * int(K)

if limitTime > int(M):
    print("NO")
else:
    print("YES")