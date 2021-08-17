while True:
    sides = list(map(int, input().split()))
    if sides == [0, 0, 0]:
        break
    sides = sorted(sides)
    if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
        print("right")
    else:
        print("wrong")
