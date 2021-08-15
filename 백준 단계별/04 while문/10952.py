A, B = map(int, input().split())

while A != 0 or B != 0:
    print(A + B)
    A, B = map(int, input().split())

# 더 나은 풀이 ↓
# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)