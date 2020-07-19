arr = [100,-23,-23,404,100,23,23,23,3,404]

arr = [6,1,9]
arr = [11,22,7,7,7,7,7,7,7,22,13]

arr = [7]
arr = [7,6,9,6,9,6,9,7]

from random import randint

arr = [randint(-10**8,10**8) for i in range(10**4)]

from collections import deque, defaultdict

def build_graph(arr):
    graph = defaultdict(set)
    for i,j in enumerate(arr):
        if i+1 < len(arr):
            graph[i].add(i+1)
        if i-1 >=0:
            graph[i].add(i-1)
        for x,y in enumerate(arr):
            if j == y and i!=x:
                graph[i].add(x)
    return graph

def bfs(graph,end):
    visited = set()
    visited.add(0)
    queue = deque([(0,0)])
    while queue:
        item = queue.popleft()
        if item[0] == end:
            return item[1]
        nbors = graph[item[0]]
        for nbor in nbors:
            if nbor not in visited:
                visited.add(nbor)
                queue.append((nbor,item[1]+1))
    

def sol(arr):
    g = build_graph(arr)
    return bfs(g,len(arr)-1)

print(sol(arr))