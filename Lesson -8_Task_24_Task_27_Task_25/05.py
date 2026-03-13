from math import dist

clustersA = ([], [])
clustersB = ([], [], [], [], [])

with open('05_27_A.txt') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x < 0:
            clustersA[0].append((x, y))
        else:
            clustersA[1].append((x, y))
print(*(len(kl) for kl in clustersA), '|', cnt)

with open('05_27_B.txt') as file:
    cnt = 0
    for s in file:
        cnt += 1
        x, y = map(float, s.split())
        if x < 0:
            clustersB[0].append((x, y))
        elif 0 < x < 4:
            clustersB[1].append((x, y))
        elif 12 < x < 16:
            clustersB[2].append((x, y))
        elif 22 < x < 26:
            clustersB[3].append((x, y))
        else:
            clustersB[4].append((x, y))
print(*(len(kl) for kl in clustersB), '|', cnt)


def get_centroid_acentroid(kl):
    res = []
    for point in kl:
        sum_dist = sum(dist(point, p) for p in kl)
        res.append((sum_dist, point))
    return min(res)[1], max(res)[1]


centroids_acentroidsA = tuple(get_centroid_acentroid(kl) for kl in clustersA)
centroids_acentroidsB = tuple(get_centroid_acentroid(kl) for kl in clustersB)

Sx = abs(int(sum(x[0] + y[0] for x, y in centroids_acentroidsA) * 1000))
Sy = abs(int(sum(x[1] + y[1] for x, y in centroids_acentroidsA) * 1000))

Qx = int(max(abs(x[0] - y[0]) for x, y in centroids_acentroidsB) * 1000)
Qy = int(min(abs(x[1] - y[1]) for x, y in centroids_acentroidsB) * 1000)

print(Sx, Sy)
print(Qx, Qy)
