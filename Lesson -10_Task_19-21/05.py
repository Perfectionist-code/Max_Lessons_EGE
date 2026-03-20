def f(s1, s2, m):
    if s1 + s2 >= 151: return m % 2 == 0
    if m == 0: return 0
    h = (f(s1 + 1, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1 * 4, s2, m - 1), f(s1, s2 * 4, m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


# если у нас в задаче сказано, что Ваня выиграл первым ходом после неудачного хода
# Пети, то после else, all меняем на any, иначе всегда после else all

print('19)', *(s for s in range(1, 142) if f(9, s, 2)))  # 7
print('20)', *(s for s in range(1, 142) if not f(9, s, 1) and f(9, s, 3)))  # 6 35
print('21)', *(s for s in range(1, 142) if not f(9, s, 2) and f(9, s, 4)))  # 34
