dwarf = []
for _ in range(9):
    dwarf.append(int(input()))

for i in range(8):
    finish = False
    for j in range(i+1, 9):
        new_dwarf = list(dwarf)
        new_dwarf.pop(i)
        new_dwarf.pop(j-1)
        if sum(new_dwarf) == 100:
            finish = True
            break
    if finish:
        break

new_dwarf.sort()

print('\n'.join([str(i) for i in new_dwarf]))
