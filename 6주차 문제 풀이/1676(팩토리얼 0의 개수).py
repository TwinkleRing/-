n = int(input())
fac = 1
for i in range(1, n + 1):
    fac = fac * i

number = list(str(fac))


count = 0
number = number[::-1]
for i in number:
    if i == '0' :
        count += 1
    if i != '0' :
        break

print(count)
