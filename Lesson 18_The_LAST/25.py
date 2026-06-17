# def is_prime(n):
#     return n > 1 and all(n % d != 0 for d in range(2, int(n ** 0.5) + 1))


def fact(n, p=2):
    for d in range(p, int(n ** .5) + 1):
        if n % d == 0:
            return [d] + fact(n // d, d)
    return [n]


cnt = 0
for num in range(6_300_001, 10 ** 10):
    prime_divs = fact(num)
    if len(prime_divs) > 1:
        m = prime_divs[0] + prime_divs[-1]
        if m > 90000 and (m ** 0.5).is_integer():
            print(num, m)
            cnt += 1
        if cnt == 5:
            break
