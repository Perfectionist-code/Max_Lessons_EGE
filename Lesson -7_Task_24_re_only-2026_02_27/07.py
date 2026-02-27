from re import *

with open('07.txt') as file:
    s = file.readline()
print((ls:=len(s)))

reg = r'([1-9AB][0-9AB]*[02468A])'
reg = fr'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m), m)