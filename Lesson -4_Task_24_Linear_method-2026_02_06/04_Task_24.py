# метод 1
# with open('04_24.txt') as f:
#     s = f.readline()
# while 'XX' in s or 'YY' in s or 'ZZ' in s:
#     s = s.replace('XX', 'X X').replace('YY', 'Y Y').replace('ZZ', 'Z Z')
# s = s.split()
# print(len(max(s,key=len)))


# метод 2
# with open('04_24.txt') as f:
#     s = f.readline()
# print((ls := len(s)))
#
# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if all(c[i] != c[i - 1] for i in range(1, len(c))):
#             m = max(m, len(c))
#             print(c)
#         else:
#             break
# print(m)

