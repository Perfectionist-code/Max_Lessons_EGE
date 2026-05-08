from functools import lru_cache
from fractions import Fraction


@lru_cache(1000)
def g(n):
    if n < 31: return 4
    return Fraction(n, 2) * g(n - 2)


@lru_cache(3)
def f(n):
    if n < 14: return 8 * g(n - 3)
    return n * f(n - 1)

print('Начинаем вычислять G:')
for i in range(30, 641_451):
    if i % 10_000 == 0: print(i)
    g(i)
print('Начинаем вычислять F:')
for i in range(13, 320727):
    if i % 10_000 == 0: print(i)
    f(i)

print(f(320726) / g(641450))
