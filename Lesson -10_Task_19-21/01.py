def f(s, m):
    if s >= 54: return m % 2 == 0
    if m == 0: return 0
    h = (f(s + 1, m - 1), f(s * 2, m - 1))
    return any(h) if (m - 1) % 2 == 0 else all(h)

# если у нас в задаче сказано, что Ваня выиграл первым ходом после неудачного хода
# Пети, то после else, all меняем на any, иначе всегда после else all

print('19)', *(s for s in range(1,54) if f(s, 2))) # 14
print('20)', *(s for s in range(1,54) if not f(s, 1) and f(s, 3))) # 13 25
print('21)', *(s for s in range(1,54) if not f(s, 2) and f(s, 4))) # 24
