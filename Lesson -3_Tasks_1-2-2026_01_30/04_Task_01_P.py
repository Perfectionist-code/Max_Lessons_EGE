from itertools import permutations

table = '1345 2367 31267 4156 5147 6234 7235'
graph = 'АБВГ БАДЖ ВАГЕ ГАВД ДГЕБЖ ЕВДЖ ЖБДЕ'

print(*'1234567')
graph = {x[0]: set(x[1:]) for x in graph.split()}

for per in permutations('АБВГДЕЖ'):
    new_graph = table
    for x, y in zip('1234567', per):
        new_graph = new_graph.replace(x,y)
    new_graph = {x[0]: set(x[1:]) for x in new_graph.split()}
    if new_graph == graph:
        print(*per)







# a = [1,2,3,4,5,6,7, '@']
# b = ['A','B', 1,3,5,'C','D', 1 ,2, 4]
# print(list(zip(a,b)))