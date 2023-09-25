notSelfNumList = set()
for i in range(1, 10001):
    if i == 1 or i not in notSelfNumList:
        print(i)

    notSelfNumList.add(i + sum(map(int, list(str(i)))))
