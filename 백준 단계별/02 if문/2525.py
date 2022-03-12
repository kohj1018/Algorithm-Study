A, B = map(int, input().split())
C = int(input())

C_hour = C // 60
C_min = C % 60

A += C_hour
B += C_min

if B >= 60:
    B -= 60
    A += 1
if A >= 24:
    A -= 24

print(A, B)