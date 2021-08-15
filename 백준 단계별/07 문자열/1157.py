word = input().upper()

lotAlp = '?'
maxCnt = 0
for alp in set(word):
    if word.count(alp) > maxCnt:
        maxCnt = word.count(alp)
        lotAlp = alp
    elif word.count(alp) == maxCnt:
        lotAlp = '?'
print(lotAlp)


# for alp in "ABCDEFGHIJKLMNOPQRSTUVWXYZ": 이 부분에서
# for alp in set(word): 로 하는 것도 괜찮은 풀이 같다.
