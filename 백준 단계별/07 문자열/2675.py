T = int(input())
for _ in range(T):
    R, S = input().split()
    text = ""
    for alp in S:
        text += alp * int(R)
    print(text)
