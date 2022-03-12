"""
1. 아이디어
우선 여는 괄호 '('나 '['가 들어올 때는 스택에 넣는다.
그리고 닫는 괄호 ')'나 ']'가 나오면 스택에서 pop해서 비교한다.
비교했는데 둘이 다른 종류면 그 즉시 종료하고 0을 출력
닫는 괄호 나오면 pop한다. pop했는데 숫자가 나오면 또 pop한다.
그렇게 계속 pop해서 숫자가 안나올때까지하고 pop해서 나온 숫자들은 모두 더한다.
그리고 그 더한 숫자들에다가 괄호 값을 곱한다. 그리고 다시 스택에 집어넣는다.
이를 반복하고 공백이 나오면 종료한다.(문자열 마지막에 공백 넣기)

2. 시간복잡도
- O(n)

3. 자료구조
parentheses: str;
stack: str[];
"""
import sys
from collections import deque

input = sys.stdin.readline

parentheses = input()
stack = deque()
stack.append(parentheses[0])
for pare in parentheses[1:]:
    fetch = False
    if fetch or pare == '\n':
        break
    if pare == ")":
        if not stack or stack[-1] == "[":   # 잘못된 괄호열
            print(0)
            break
        elif stack[-1] == "(":              # 값을 반환해야 하는 경우
            stack.pop()
            stack.append("2")
        else:                               # 숫자가 있는 경우 (stack[-1]의 값이 숫자)
            midResult = int(stack.pop())
            while 1:
                if stack[-1] == "[":
                    print(0)
                    fetch = True
                    break
                elif stack[-1] == "(":
                    stack.pop()
                    stack.append(str(2 * midResult))
                    break
                else:
                    midResult += int(stack.pop())
    elif pare == "]":
        if not stack or stack[-1] == "(":   # 잘못된 괄호열
            print(0)
            break
        elif stack[-1] == "[":              # 값을 반환해야 하는 경우
            stack.pop()
            stack.append("3")
        else:
            midResult = int(stack.pop())
            while 1:
                if stack[-1] == "(":
                    print(0)
                    fetch = True
                    break
                elif stack[-1] == "[":
                    stack.pop()
                    stack.append(str(3 * midResult))
                    break
                else:
                    midResult += int(stack.pop())
    else:
        stack.append(pare)

print(sum(map(int, stack)))