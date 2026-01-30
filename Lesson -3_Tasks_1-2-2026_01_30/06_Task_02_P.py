from itertools import product, permutations


def f(x, y, w, z):
    return (z == (not x)) <= ((w <= (not y)) and (y <= x))


for a1, a2, a3, a4, a5 in product((0, 1), repeat=5):
    table = ((1, 1, 1, 0), (a1, a2, 0, 0), (a3, 0, a4, a5))
    if len(set(table)) == 3:
        for per in permutations('xywz'):
            if [f(**dict(zip(per, row))) for row in table] == [1, 0, 0]:
                print(*per, sep='')
