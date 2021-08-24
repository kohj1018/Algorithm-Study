n = int(input())

numList = []
for _ in range(n):
    numList.append(int(input()))

stack = []
result = []
cursor = 0
for i in range(1, n+1):
    stack.append(i)
    result.append("+")
    while cursor < n and stack and numList[cursor] == stack[-1]:
        stack.pop()
        result.append("-")
        cursor += 1

# 만약 stack이 비지 않았다면 입력된 수열을 만들지 못했다는 뜻
if stack:
    print("NO")
else:
    for c in result:
        print(c)
