N, X = map(int, input().split())
A = [int(a) for a in input().split()]

for i in range(N):
    if A[i] < X:
        print(A[i], end=' ')
