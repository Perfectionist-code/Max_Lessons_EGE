from re import *

with open('05.txt') as file:
    s = file.readline()
print((ls:=len(s)))

reg = r'(LMN|MN|N){0,1}(KLMN)+(KLM|KL|K){0,1}'
m = max((x.group() for x in finditer(reg, s)), key=len)
print(len(m), m)