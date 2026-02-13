with open('06_24.txt') as file:
    s = file.readline()
print((ls := len(s)))

s = s.replace('B', 'A').replace('C', 'A')
for char in '6789':
    s = s. replace(char, '1')

m = 0
for l in range(ls):
    for r in range(l + m, ls):
        c = s[l:r + 1]
        if all(c[i:i + 2] not in ('AA', '11') for i in range(0, len(c) - 1)):
            m = max(m, len(c))
            print(c)
        else:
            break
print(m)