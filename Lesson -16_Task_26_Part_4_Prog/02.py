with open('02.txt') as file:
    n, m = map(int, file.readline().split())
    teams = []
    planes = []
    for _ in range(n):
        teams.append(int(file.readline()))
    for _ in range(m):
        planes.append(int(file.readline()))
teams.sort(reverse=True)
planes.sort(reverse=True)
tickets = []
while planes and teams:
    plane = planes.pop(0)
    while teams:
        team = teams.pop(0)
        if team * 2 <= plane:
            tickets.append((team, plane))
            break
print(tickets)
print(teams)
print(planes)
print(len(tickets), max(tickets)[0])