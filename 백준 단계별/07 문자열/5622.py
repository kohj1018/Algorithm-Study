dials = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

STR = input()

time = 0
for letter in STR:
    for i, dial in enumerate(dials):
        if letter in dial:
            time += 2 + 1 * (i + 1)
print(time)