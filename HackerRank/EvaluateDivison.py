

equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]




# for i,j in zip(equations,values):   
#     graph[i[0]].append({i[1]:j})
#     graph[i[1]].append({i[0]:float("{:.1f}".format(1/j))})


from collections import defaultdict
from collections import deque

def bfs(graph,start,end):

	if start not in graph or end not in graph:
		return -1.0
	if start == end:
		return 1.0
	visited = set()
	visited.add(start)
	queue = deque([[start]])
	while queue:
		path = queue.popleft()
		item = path[-1]
		nbors = graph[item]
		if end in nbors:
			return path+[end]
		for nbor in nbors:
			if nbor not in visited:
				visited.add(nbor)
				queue.append(path+[nbor])
	return -1.0


def sol(equations, values, queries):
	graph = defaultdict(list)
	for i in equations:   
		graph[i[0]].append(i[1])
		graph[i[1]].append(i[0])

	l = []
	for query in queries:
		path = bfs(graph,*query)
		l.append(path)
	for i in l:
		print(i)
	
	for i,j in zip(equations,values):
		equations.append([i[1],i[0]])
		values.append(float(1/j))
	

	for _ in range(len(l)):
		if type(l[_])==float:
			continue
		m = 1
		for i in range(len(l[_])-1):
			indx = equations.index([l[_][i],l[_][i+1]])
			m*=values[indx]
		l[_] = m
	return l
			
a = [["a","e"],["b","e"]]
b = [4.0,3.0]
c = [["a","b"],["e","e"],["x","x"]]

a = [["a","b"],["c","d"]]
b = [1.0,1.0]
c = [["a","c"],["b","d"],["b","a"],["d","c"]]
	
k = sol(a,b,c)

print(k)
