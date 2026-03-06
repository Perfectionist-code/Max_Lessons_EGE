# with open('01.txt') as file:
#     s = file.readline()
# print((ls := len(s)))
#
# m = 200000
# for l in range(ls):
#     for r in range(l + m, ls):
#         c = s[l:r + 1]
#         if (sm := sum(c[i] == c[i + 1] for i in range(len(c) - 1))) <= 100_000:
#             if sm == 100000:
#                 m = max(m, len(c))
#                 print(m)
#         else:
#             break
# print(m)

with open('01.txt') as file:
    s = file.readline()
print((ls := len(s)))

max_length = 0
current_length = 0
bad_count = 0
start_pos = 0

# Проходим по всем символам файла
for i in range(ls):
    # Проверка, является ли текущая позиция символов плохой
    if i > 0 and s[i] == s[i - 1]:
        bad_count += 1

    # Если количество "плохих" подстрок превысило K=10000, сдвигаем влево начальную позицию
    while bad_count > 100000:
        if s[start_pos] == s[start_pos + 1]:
            bad_count -= 1
        start_pos += 1

    # Обновляем текущую длину последовательности
    current_length = i - start_pos + 1

    # Проверяем условие и обновляем максимум длины
    if bad_count == 100000 and current_length > max_length:
        max_length = current_length

print(max_length)
