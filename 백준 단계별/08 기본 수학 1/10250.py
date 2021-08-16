T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        floor = H
        num = N // H
    else:
        floor = N % H
        num = N // H + 1
    print("{0:d}{1:02d}".format(floor, num))
