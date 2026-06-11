def f(x, y):
    return (21757691 != 19 * x + 3 * y) and (718433 != 5 * x + 2 * y) or (A > x) or (A > y)


pairs1 = [(x, (21757691 - 19 * x) / 3) for x in range(1, 1145145)]
pairs1 = set([(x, int(y)) for x, y in pairs1 if y > 0 and y.is_integer()])
# print(pairs1)
pairs2 = [(x, (718433 - 5 * x) / 2) for x in range(1, 143700)]
pairs2 = set([(x, int(y)) for x, y in pairs1 if y > 0 and y.is_integer()])
c = pairs1 | pairs2

print('Finding A')
for A in range(3589067349857349857):
    if all(f(x, y) for x, y in c):
        print(A)
        break
