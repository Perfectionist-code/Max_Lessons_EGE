from itertools import product, permutations


def f1(x, y, w, z):
    return (x <= y) == (w or (not z))


def f2(x, y, w, z):
    return (x <= y) and ((not w) == z)


for a1, a2, a3, b1, b2 in product((0, 1), repeat=5):
    table = ((a1, 1, 0, 1), (a2, 0, 0, 0), (0, a3, 0, 0))
    if len(set(table)) == 3:
        for per in permutations('xywz'):
            if [f1(**dict(zip(per, row))) for row in table] == [b1, 0, 0] and [f2(**dict(zip(per, row))) for row in
                                                                               table] == [0, b2, 1]:
                print(*per, sep='')
