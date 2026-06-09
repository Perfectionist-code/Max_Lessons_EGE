# def f(x, y):
#     return (49531739 != 14 * y + 15 * x) or (A < x) or (A < y)
#
#
# for A in range(1708000, 0, -1):
#     if all(f(x, y) for x in range(1707000, 1709000) for y in range(1707000, 1709000)):
#         print(A)
#         break

def f(x, y):
    return (49531739 != 14 * y + 15 * x) or (A < x) or (A < y)


pairs = set((x, (49531739 - 15 * x) // 14) for x in range(1, 3302117) if 49531739 - 15 * x > 0 and (49531739 - 15 * x) % 14 == 0)
print(len(pairs))

for A in range(2000000, 0, -1):
    if all(f(x, y) for x, y in pairs):
        print(A)
        break
