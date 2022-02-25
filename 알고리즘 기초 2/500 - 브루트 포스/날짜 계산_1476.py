E, S, M = map(int, input().split())
e, s, m, year = 0, 0, 0, 0
while 1:
    e += 1
    s += 1
    m += 1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
    year += 1
    if e == E and s == S and m == M:
        break
print(year)
