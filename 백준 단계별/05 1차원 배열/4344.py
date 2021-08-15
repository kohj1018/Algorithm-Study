C = int(input())

for _ in range(C):
    TC = list(map(int, input().split()))
    avg = ( sum(TC) - TC[0] ) / TC[0]
    cnt = 0
    for i in range(1, TC[0] + 1):
        if TC[i] > avg:
            cnt += 1
    print("{0:.3f}%".format( cnt / TC[0] * 100 ))
