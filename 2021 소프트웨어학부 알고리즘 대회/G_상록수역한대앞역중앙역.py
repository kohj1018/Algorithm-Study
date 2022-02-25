A, B, C = map(int, input().split())

if A > B:
    if B > C:
        print("GO JUNG")
    else:
        print("GO HAN")
else:
    if A > C:
        print("GO JUNG")
    else:
        print("GO SANG")
