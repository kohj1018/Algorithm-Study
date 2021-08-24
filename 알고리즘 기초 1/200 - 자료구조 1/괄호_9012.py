T = int(input())

for _ in range(T):
    parenthesis = input() + " "
    stack = []
    VPS = False
    for char in parenthesis:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                break
        else:
            if len(stack) == 0:
                VPS = True
    if VPS:
        print("YES")
    else:
        print("NO")
