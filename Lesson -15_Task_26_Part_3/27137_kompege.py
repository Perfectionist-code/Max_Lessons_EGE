pairs1 = set([(x, 1241651 - 5 * x) for x in range(1, 250000) if 1241651 - 5 * x > 0])
pairs2 = [(x, (413184 - x) // 2) for x in range(1, 250000) if 413184 - x > 0 and (413184 - x) % 2 == 0]
c = pairs1.union(pairs2)
print(len(c))

def f(x, y):
    return (1241651 != 5 * x + y) and (413184 != x + 2 * y) or (A > x) or (A > y)

for A in range(1, 2000000):
    if all(f(x,y) for x,y in c):
        print(A)
        break
