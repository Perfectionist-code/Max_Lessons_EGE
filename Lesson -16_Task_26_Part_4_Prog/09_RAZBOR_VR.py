with open('09.txt') as file:
    m = None
    for s in file:
        l = list(map(int, s.split()))
        l_rep_2 = [x for x in l if l.count(x) == 2]
        l_rep_3 = [x for x in l if l.count(x) == 3]
        l_rep = l_rep_2 + l_rep_3
        l_fr = [x for x in l if l.count(x) == 1]
        if len(set(l_rep_3)) == len(set(l_rep_2)) == len(set(l_fr)) == 1 and l_fr[0] <= min(l_rep):
            m = min(l_rep)
print(abs(m))
