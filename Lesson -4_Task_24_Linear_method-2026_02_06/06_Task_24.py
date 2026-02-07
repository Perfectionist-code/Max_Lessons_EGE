# метод 1
# with open('06_24.txt') as f:
#     s = f.readline()
# s = s.replace('ad', 'a d').replace('da', 'd a').split()
# print(len(max(s,key=len)))

# метод 2
# with open('06_24.txt') as f:
#     s = f.readline()
# print((ls := len(s)))
#
# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if 'ad' not in c and 'da' not in c:
#             m = max(m, len(c))
#             print(c)
#         else:
#             break
# print(m)

# метод 3
from re import *

with open('06_24.txt') as f:
    s = f.readline()
print((ls := len(s)))
s = s.replace('ad', 'a#d').replace('da', 'd#a')
reg = r'[^#]*'
reg = fr'(?=({reg}))'
m = max([x.group(1) for x in finditer(reg, s)], key=len)
print(len(m), m)
