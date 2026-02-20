from re import *

with open('07.txt') as file:
    s = file.readline()
print((ls:=len(s)))

num = r'([1-9][0-9]*|0)'
expression = fr'({num}\*)*0(\*{num})*'
expression = fr'{expression}(\+{expression})*'
reg = fr'{expression}(\+{expression})*'
# reg = fr'(?=({expression}))'
m = max([x.group() for x in finditer(reg,s)], key=len)
print(len(m), m)