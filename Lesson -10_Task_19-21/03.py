def f(s, m):
    if s <= 19: return m % 2 == 0
    if m == 0: return 0
    h = (f(s - 2, m - 1), f(s - 5, m - 1), f(s // 3, m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)


# если у нас в задаче сказано, что Ваня выиграл первым ходом после неудачного хода
# Пети, то после else, all меняем на any, иначе всегда после else all

print('19)', *(s for s in range(20, 300) if f(s, 2)))  # 60
print('20)', *(s for s in range(20, 300) if not f(s, 1) and f(s, 3)))  # 62 63
print('21)', *(s for s in range(20, 300) if not f(s, 2) and f(s, 4)))  # 64
