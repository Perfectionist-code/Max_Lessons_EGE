# with open('03_24.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
# s = s.replace('O', 'A')
# for char in 'CD':
#     s = s.replace(char, 'B')
#
# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if len(c) % 2 == 0:
#             if all(c[i:i + 2] == 'BA' for i in range(0, len(c), 2)):
#                 m = max(m, len(c))
#                 print(c)
#             else:
#                 break
# print(m // 2)

# метод re
from re import *

with open('03_24.txt') as file:
    s = file.readline()
print((ls := len(s)))

reg = r'(BA|CA|DA|BO|CO|DO)+'
reg = fr'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)

print(len(m) // 2, m)
