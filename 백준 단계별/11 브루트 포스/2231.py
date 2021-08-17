N = int(input())

generator = 0
for i in range(1, N):
    digit_sum = i + sum(map(int, str(i)))
    if digit_sum == N:
        generator = i
        break
print(generator)
