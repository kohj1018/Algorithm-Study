a, b = map(int, input().split())

greatDivisor = 1
for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        greatDivisor = i

print(greatDivisor)
print(greatDivisor * (a // greatDivisor) * (b // greatDivisor))
