# 내가 푼 풀이
N = int(input())

a = N // 5
b = 0
while a != -1 and N != (5 * a) + (3 * b):
    if b <= N // 3:
        b += 1
        continue
    else:
        b = 0
        a -= 1

if a == -1:
    print(-1)
else:
    print(a + b)
