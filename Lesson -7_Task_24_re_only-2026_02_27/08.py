# from re import *
#
# with open('08.txt') as file:
#     s = file.readline()
# print((ls:=len(s)))
#
# num = r'([1-9][0-9]*|0)'
# expression = fr'({num}\*)*0(\*{num})*'
# expression = fr'{expression}+(\+{expression})*'
# reg = fr'(?=({expression}))'
# m = max((x.group(1) for x in finditer(reg, s)), key=len)
# print(len(m), m)

from re import *

with open('08.txt') as file:
    s = file.readline()
print((ls:=len(s)))

num = r'([1-9][0-9]*|0)'
expression = fr'({num}([\+\*]{num})*)'
reg = fr'(?=({expression}))'
m = tuple(x.group(1) for x in finditer(reg, s))
m = max((x for x in m if not x.isdigit() and eval(x) == 0), key=len)
print(len(m), m)