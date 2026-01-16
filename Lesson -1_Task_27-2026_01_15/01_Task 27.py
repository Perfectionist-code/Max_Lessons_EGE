from math import dist

clustersA = ([], [])
clustersB = ([], [], [])

with open('01_27var01A.txt') as file:
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if x > 0 and y > 16:
            clustersA[0].append((x, y))
        elif x > 0 and 10 < y < 15:
            clustersA[1].append((x, y))
print(*(sm := tuple(len(kl) for kl in clustersA)), '|', sum(sm))

with open('01_27var01B.txt') as file:
    for s in file:
        s = s.replace(',', '.')
        x, y = map(float, s.split())
        if x > 12 and 13 < y < 19:
            clustersB[0].append((x, y))
        elif 13 < x < 18 and 6 < y < 13:
            clustersB[1].append((x, y))
        elif 23 < x < 29:
            clustersB[2].append((x, y))
print(*(sm := tuple(len(kl) for kl in clustersB)), '|', sum(sm))


def get_centroid(kl):
    res = []
    for point in kl:
        sum_dist = sum(dist(point, p) for p in kl)
        res.append((sum_dist, point))
    return min(res)[1]


centroidsA = tuple(get_centroid(kl) for kl in clustersA)
centroidsB = tuple(get_centroid(kl) for kl in clustersB)
print('---' * 5)


def get_P():
    dist_cent_point = [dist(centroidsA[i], p) for i in range(2) for p in clustersA[-1 + i]]
    return min(dist_cent_point), max(dist_cent_point)


def get_Q(n_kl):
    return int(sum(dist(centroidsB[n_kl], p) for p in clustersB[n_kl]) / (len(clustersB[n_kl]) - 1) * 10_000)


print(*(abs(int(x * 10_000)) for x in get_P()))
print(*(get_Q(n) for n in (0,2)))
