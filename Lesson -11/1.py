# # from statistics import mean
# #
# # sm = 0
# # with open('9.txt') as file:
# #     for i, s in enumerate(file, 1):
# #         if not i % 2:
# #             l = list(map(int, s.split()))
# #             m_l = mean(l)
# #             if any(x == int(m_l) for x in l) and any((x ** 0.5).is_integer() for x in l):
# #                 sm += i
# #                 print(*l)
# # print('---' * 5)
# # print(sm)
#
# from math import prod
#
#
# def get_r(n: int):
#     nums_in_n = [int(x) for x in str(n)]
#     p = prod(x for x in nums_in_n if x != 0)
#     m = max(nums_in_n) + min(nums_in_n)
#     t_1 = p + m
#     t_2 = p * m
#     pr = sorted((t_1, t_2))
#     r = str(pr[0]) + str(pr[1])
#     return int(r)
#
#
# # print(get_r(234))
#
# for num in range(10000, 0, -1):
#     if get_r(num) == 23126:
#         print(num)
#         break
#
# #72
#
# from itertools import product
#
# res = set()
# for pr in product('0123456789AB', repeat=5):
#     if pr[0] != '0':
#         num = ''.join(pr)
#         num1 = num
#         for char in '02468A':
#             num1 = num1.replace(char, '*')
#         if num1.count('*') == 3 and '***' in num1 and any(x * 3 in num for x in '02468A'):
#             res.add(num)
#             print(num, num1)
# print(len(res))

a = 'sdfsdfgsdfgfdgdf'
a = list(a)
print(a)
n = ' '.join(a)
print(n)
# 22032