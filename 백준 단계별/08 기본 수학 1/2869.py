A, B, V = map(int, input().split())

pre_move = (V-A) // (A-B)
remainder = (V-A) % (A-B)

if remainder > 0:
    print(pre_move + 2)
else:
    print(pre_move + 1)
