with open('02.txt') as file:
    s = file.readline()
print((ls := len(s)))

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if sum(c.count(x)for x in 'AEIOUY') <=5:
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)