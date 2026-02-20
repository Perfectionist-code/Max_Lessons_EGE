with open('04.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 10000
for l in range(ls):
    for r in range(l + m, l, -1):
        c = s[l:r + 1]
        if c.count('Z') >= 120:
            m = min(m, len(c))
            print(c)
        else:
            break
print(m)
