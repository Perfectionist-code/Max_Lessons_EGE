# метод 2
# with open('07_24.txt') as f:
#     s = f.readline()
# print((ls := len(s)))
#
# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if 'XZZY' not in c:
#             m = max(m, len(c))
#             print(c)
#         else:
#             break
# print(m)
