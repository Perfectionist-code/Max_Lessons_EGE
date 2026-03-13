from math import prod


def fact(n, p=2):
    for d in range(p, int(n ** .5) + 1):
        if n % d == 0:
            return [d] + fact(n // d, d)
    return [n]


def get_divisors(n):
    res = set()
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return res


def is_prime(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))

# cnt = 0
# for num in range(2_142_578, 10 ** 8):
#     prime_divs = fact(num)
#     if len(prime_divs) == 2 and num == prod(prime_divs) and sum(prime_divs) % 2:
#         cnt += 1
#         print(num, max(prime_divs))
#     if cnt == 5:
#         break

cnt = 0
for num in range(2_142_578, 10 ** 8):
    divs = get_divisors(num)
    prime_divs = [x for x in divs if is_prime(x)]
    if len(prime_divs) == 2 and num == prod(prime_divs) and sum(prime_divs) % 2:
        cnt += 1
        print(num, max(prime_divs))
    if cnt == 5:
        break