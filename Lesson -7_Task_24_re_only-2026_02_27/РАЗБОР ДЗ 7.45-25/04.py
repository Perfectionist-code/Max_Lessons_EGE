from re import *

with open('04.txt') as file:
    s = file.readline()
print((ls:=len(s)))

num = r'([1-5][0-5]*|0)'
expression = fr'({num}(\*{num})*(\-{num})*)'
reg = fr'(?=({expression}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)
print(eval(m))