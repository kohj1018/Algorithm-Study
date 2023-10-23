N = input()
if int(N) < 10:
    N = '0' + N

newN = N

i = 0
while True:
    newN = str(newN[1])[-1] + str(int(newN[0]) + int(newN[1]))[-1]
    i += 1
    if newN == N:
        print(i)
        break
