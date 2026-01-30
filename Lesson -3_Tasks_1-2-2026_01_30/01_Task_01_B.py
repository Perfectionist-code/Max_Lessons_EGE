from itertools import permutations

table = '1246 216 357 415 5347 6127 7356'
graph = 'AGBC BGEA CDFA DFC EBF FCDE GBA'

print(*'1234567')
graph = {x[0]: set(x[1:]) for x in graph.split()}

for per in permutations('ABCDEFG'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x,y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph:
        print(*per)







# a = [1,2,3,4,5,6,7, '@']
# b = ['A','B', 1,3,5,'C','D', 1 ,2, 4]
# print(list(zip(a,b)))