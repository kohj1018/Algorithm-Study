Croatia_alp = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()

cursor = 0
cnt = 0
while cursor < len(word):
    if word[cursor : cursor+3] in Croatia_alp:
        cursor += 3
    elif word[cursor : cursor+2] in Croatia_alp:
        cursor += 2
    else:
        cursor += 1
    cnt += 1

print(cnt)


# 더 괜찮은 풀이 ↓
# a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# alpha = input()
#
# for t in a:
#     alpha = alpha.replace(t, '*')
#
# print(len(alpha))
