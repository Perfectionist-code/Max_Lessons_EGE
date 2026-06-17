def f(curr, end, cnt=0):
    if curr > end or curr in (28, 36): return 0
    if curr in (18, 30): cnt += 1
    if curr == end: return cnt == 2
    return f(curr + 1, end, cnt) + f(curr + 5, end, cnt) + f(curr * 3, end, cnt)

print(f(2, 49))
