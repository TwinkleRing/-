from itertools import combinations as cb
dwarf = []
for i in range(9) :
    dwarf.append(int(input()))

aim_num = sum(dwarf) - 100

candidates = list(cb(dwarf, 2))
for i, j in candidates :
    sum1 = int(i) + int(j)
    if sum1 == aim_num :
        dwarf.remove(i)
        dwarf.remove(j)
        break

dwarf.sort()
for i in dwarf :
    print(i, end = "\n")