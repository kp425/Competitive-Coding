routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6

routes = [set(i) for i in routes]

for i in routes:
    print(i)

print(routes[1].intersection(routes[0]))