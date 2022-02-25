N, M = map(int, input().split())

def check(x, y):
    if x > 0 and room[x-1][y] == '1': return False
    if y > 0 and room[x][y-1] == '1': return False
    if N-1 > x and room[x+1][y] == '1': return False
    if M-1 > y and room[x][y+1] == '1': return False
    return True

room = []

studentNum = 0
totNum = N * M
for _ in range(N):
    col = list(input())
    studentNum += col.count('1')
    room.append(col)

cnt = 0
for i in range(N):
    for j in range(M):
        if room[i][j] == '0': continue
        if check(i, j) == False: cnt += 1
isOK = False
if cnt == 0: isOK = True

if totNum % 2 == 0:
    if totNum // 2 >= studentNum:
        isOK = True
else:
    if totNum // 2 + 1 >= studentNum:
        isOK = False

print(cnt)
if isOK:
    print("YES")
else:
    print("NO")
