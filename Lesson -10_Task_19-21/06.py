def f(s1, s2, m):
    if s1 + s2 >= 65: return m % 2 == 0
    if m == 0: return 0
    h = (f(s1 + 1, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1 * 3, s2, m - 1), f(s1, s2 * 3, m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


# если у нас в задаче сказано, что Ваня выиграл первым ходом после неудачного хода
# Пети, то после else, all меняем на any, иначе всегда после else all

print('19)', *(s for s in range(1, 59) if f(6, s, 2)))  # 7
print('20)', *(s for s in range(1, 59) if not f(6, s, 1) and f(6, s, 3)))  # 10 19
print('21)', *(s for s in range(1, 59) if not f(6, s, 2) and f(6, s, 4)))  # 18
