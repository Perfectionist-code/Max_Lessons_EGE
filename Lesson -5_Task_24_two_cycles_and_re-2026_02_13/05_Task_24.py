with open('05_24.txt') as file:
    s = file.readline()
print((ls := len(s)))

s = s.replace('Q', '*').replace('R', '*').replace('S', '*')

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if all(c[i:i + 2] != '**' for i in range(len(c) - 1)):
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)

