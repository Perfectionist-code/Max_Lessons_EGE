def f(x, y):
    return (y < 3 * A) and (x < A) or (187532 < 5 * y + 17 * x)


for A in range(12400, 10 ** 10):
    if all(f(x, y) for x in range(1, 20) for y in range(37400, 37600)):
        print(A)
        break
