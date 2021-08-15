H, M = [int(i) for i in input().split()]

if M >= 45:
    print("{} {}".format(H, M - 45))
else:
    if H == 0:
        print("{} {}".format(23, 15 + M))
    else:
        print("{} {}".format(H - 1, 15 + M))
