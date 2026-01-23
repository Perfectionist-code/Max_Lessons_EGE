from math import dist
from turtle import *
from random import random

# clustersB = ([], [], [])
# with open('01_27_B.txt') as file:
#     cnt = 0
#     file.readline()
#     for s in file:
#         cnt += 1
#         s = s.replace(',', '.')
#         x, y = map(float, s.split())
#         if y > 1.5 * x + 1:
#             clustersB[0].append((x, y))
#         elif y > - 13 / 5 * x + 117 / 5:
#             clustersB[1].append((x, y))
#         else:
#             clustersB[2].append((x, y))
# print(*(sm:=tuple(len(kl) for kl in clustersB)),'|' ,sum(sm), '|',cnt )


clusters = []
with open('03_27_A.txt') as file:
    data = []
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        data.append((x, y))

while data:
    kl = [data.pop()]
    for point in kl:
        sosed = [p for p in data if dist(point, p) < 0.5]
        for p1 in sosed:
            kl.append(p1)
            data.remove(p1)
    clusters.append(kl)

print(*(len(kl) for kl in clusters))
clusters = tuple(kl for kl in clusters if len(kl) > 20)

tracer(0)
r = 20
up()
for kl in clusters:
    color = random(), random(), random()
    for point in kl:
        x, y = point
        goto(x * r, y * r)
        dot(3, color)
update()
done()  # mainloop()
