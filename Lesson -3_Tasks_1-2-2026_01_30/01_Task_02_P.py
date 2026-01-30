from itertools import product, permutations


def f(x, y, w, z):
    return (z<=w) and y and (not x)

for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    table = ((0,1,a1,0), (a2,0,a3,a4), (0,1,1,a5))
    if len(set(table)) == 3:
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [1, 1, 0]:
                print(*per, sep='')

