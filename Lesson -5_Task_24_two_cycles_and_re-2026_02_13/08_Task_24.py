# from string import ascii_uppercase as d
# with open('08_24-337.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
# for char in d[6:]:
#     s = s.replace(char, '  ')
#
# m = 0
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if c[0] != '0':
#             if c[0] == '8' and ' ' not in c:
#                 if c[-1] in '08':
#                     m = max(m, len(c))
#                     print(c)
#             else:
#                 break
# print(m)


# # метод re
# from re import *
#
# with open('08_24-337.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# num = r'([8][0-9ABCDEF]*[08])'
# reg = fr'(?=({num}))'
# m = max((x.group(1) for x in finditer(reg, s)), key=len)
#
# print(len(m), m)

with open("08_24-337.txt") as file:
    x = file.readline()
    f1 = x
    f2 = x

# способ 1
d = "0123456789ABCDEF"
m = 0
for x in range(len(f1)):
    for y in range(x + m, len(f1)):
        c = f1[x:y + 1]
        if c[0] == '8':
            if all(c[i] in "0123456789ABCDEF" for i in range(len(c))):
                if c[-1] in '08':
                    print(c)
                    m = max(m, len(c))
            else:
                break
        else:
            break
print(m)