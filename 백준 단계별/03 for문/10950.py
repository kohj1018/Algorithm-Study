T = int(input())
addList = []
for _ in range(T):
    A, B = [int(i) for i in input().split()]
    addList.append(A + B)

for result in addList:
    print(result)
