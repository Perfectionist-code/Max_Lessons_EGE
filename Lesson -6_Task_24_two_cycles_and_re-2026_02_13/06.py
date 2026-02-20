# # Метод двойного цикла
# with open('06.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if (a:=c.count('FSRQ')) <= 80:
#             if a == 80:
#                 m = max(m, len(c))
#                 print(c)
#         else:
#             break
# print(m)

# Метод re
from  re import *
with open('06.txt') as file:
    s = file.readline()
print((ls:=len(s)))

reg = r''