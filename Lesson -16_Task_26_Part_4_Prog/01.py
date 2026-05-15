with open('01.txt') as file:
    k, n = int(file.readline()),int(file.readline())
    passengers =[]
    for s in file:
        start, end = map(int, s.split())
        passengers.append((start, end))
passengers.sort()
cells = [0] * k
cnt = 0
last_cell = 0
for start, end in passengers:
    for i, cell in enumerate(cells):
        if cell < start:
            cells[i] = end
            cnt += 1
            last_cell = i + 1
            break
print(cnt, last_cell)

