# with open('07_24.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if c[0] != '0':
#             if all(x in '0123456789AB' for x in c) and c[-1] in '02468A':
#                 m = max(m, len(c))
#                 print(c)
#             else:
#                 break
#             if l % 100000 == 0: print(l, ls, m)
#         else:
#             break
# print(m)

# метод re
from re import *

with open('07_24.txt') as file:
    s = file.readline()
print((ls := len(s)))

num = r'([1-9AB][0-9AB]*[02468A])'
reg = fr'(?=({num}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)

print(len(m), m)
