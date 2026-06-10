with open('03.txt') as file:
    n, k = map(int, file.readline().split())
    land_plots = []
    snow_blowers =[]
    for _ in range(n):
        land_plots.append(int(file.readline()))
    for _ in range(k):
        power, price = map(int, file.readline().split())
        snow_blowers.append((power, price))

land_plots.sort(reverse=True)
# print(land_plots)
snow_blowers.sort(key=lambda x: (x[0], -x[1]))
# print(snow_blowers)
snow_blowers_d = dict(snow_blowers)
# print(snow_blowers_d)
res = []
for land in land_plots:
    snow_blower = min(filter(lambda x: x[0] >= land, snow_blowers_d.items()), key=lambda x:(x[1], -x[0]))
    res.append(snow_blower)
print(sum(y for x, y in res), max(res)[0])


