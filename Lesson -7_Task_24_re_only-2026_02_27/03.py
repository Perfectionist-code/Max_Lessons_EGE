from re import *

with open('03.txt') as file:
    s = file.readline()
print((ls:=len(s)))

reg = r'([BCD][AO])+'
m = max((x.group() for x in finditer(reg, s)), key=len)
print(len(m) // 2, m)