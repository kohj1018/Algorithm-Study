N = int(input())

cnt = 1
num = 666
while N > cnt:
    num += 1
    if "666" in str(num):
        cnt += 1

print(num)
