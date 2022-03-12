dwarf = [int(input()) for _ in range(9)]
totalTall = sum(dwarf)

for i in range(9-1):
    fetch = False
    for j in range(i+1, 9):
        if totalTall - (dwarf[i] + dwarf[j]) == 100:
            dwarf.pop(i)
            dwarf.pop(j-1)
            fetch = True
            break
    if fetch:
        break

dwarf.sort()
for dw in dwarf:
    print(dw)