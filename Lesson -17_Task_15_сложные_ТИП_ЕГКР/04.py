def f(x, y):
    return (5 * y < A) and (3 * x < A) or (139891 < 7 * y + 3 * x)


for A in range(139880, 10 ** 10):
    if all(f(x, y) for x in range(46000, 46650) for y in range(1, 5)):
        print(A)
        break
