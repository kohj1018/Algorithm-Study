S = input()

for alp in 'abcdefghijklmnopqrstuvwxyz':
    if alp in S:
        print(S.index(alp), end=' ')
    else:
        print(-1, end=' ')
