def f(x, y):
    return (x * y < A) or (5 * x < y) or (486 <= x)


for A in range(1176000, 2000000):
    if all(f(x, y) for x in range(490) for y in range(2430)):
        print(A)
        break
