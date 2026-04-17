res = []
for x in range(250, 350):
    for y in range(12100, 12500):
        for z in range(0, 100):
            if x + z >= 300 and (N := x + y + z) > 300 and (S := 7 * x + 8 * y + 3 * z) >= 100000:
                res.append((S + N, S, N, (x, y, z)))
print(*min(res))
