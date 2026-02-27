from re import *

with open('01.txt') as file:
    s = file.readline()
print((ls:=len(s)))

num = r'([7-9][0789]*)'
expression = fr'{num}([\-\*]{num})*'
reg = fr'(?=({expression}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)