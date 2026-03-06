# with open('06_17-10.txt') as file:
#     a = [int(x) for x in file]
# print(len(a))
#
# res = []
# for i in range(len(a)-1):
#     for j in range(i+1, len(a)):
#         if (a[i] * a[j]) % 15:
#             res.append(a[i] + a[j])
# print(len(res), max(res))

from itertools import combinations
from math import prod

with open('06_17-10.txt') as file:
    a = [int(x) for x in file]
print(len(a))

res = []
for pr in combinations(a, 2):
    if prod(pr) % 15:
        res.append(sum(pr))
print(len(res), max(res))