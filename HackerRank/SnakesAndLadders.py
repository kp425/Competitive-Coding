from collections import deque

class Vertex:
	def __init__(self,data):
		self.data = data


class Graph:

	def __init__(self):
		self.vertices = {}  #{"1":Vertex(1),"2":Vertex(2)}
		self.edges = {}     #{"1":{2:10,3:20},.....}
							
		
	def add_vertex(self, vertex):
		self.vertices[vertex] = Vertex(vertex)

	def add_edge(self, frm, to, weight= 0):
		if frm not in self.vertices:
			self.add_vertex(frm)
		if to not in self.vertices:
			self.add_vertex(to)
		if frm not in self.edges:
			self.edges[frm] = {}
		self.edges[frm][to] = weight
	
	def get_neighbors(self, vertex):
		return self.edges[vertex].keys()

	def get_vertex(self,vertex):
		return self.vertices[vertex]


def build_graph(ladders, snakes):
	graph = Graph()

	snake_cells = [i[0] for i in snakes]
	ladder_cells = [i[0] for i in ladders]

	for x in range(1,95):
		if x not in snake_cells and x not in ladders:
			for y in range(1,7):
				graph.add_edge(x,x+y)
	
	for x in range(95,100):
		if x not in snake_cells and x not in ladders:
			for y in range(1,101-x):
				graph.add_edge(x,x+y)

	# for x in range(1,95):
	# 	for y in range(1,7):
	# 		graph.add_edge(x,x+y)
	
	# for x in range(95,100):
	# 	for y in range(1,101-x):
	# 		graph.add_edge(x,x+y)
	
	for x in ladders:
		graph.add_edge(*x)
	for x in snakes:
		graph.add_edge(*x)

	return graph


def bfs(graph,start):

	visited = set()
	path = [start]
	queue = deque([(start,path)])

	while queue:
		item = queue.popleft()
		vertex = item[0]
		path = item[1]
		yield vertex,path
		for nbor in graph.get_neighbors(vertex):
			if nbor not in visited:
				visited.add(nbor)
				queue.append((nbor,path+[nbor]))

def sol(ladders, snakes):
	g = build_graph(ladders, snakes)
	l=-1
	for i in bfs(g,1):
		if i[1][-1] == 100:
			l = i[1]
			break
	if l == -1:
		return -1
	count = 0
	for i in range(len(l)-1):
		if [l[i],l[i+1]] not in l3+s3:
			count+=1
	return count



if __name__ == "__main__":

	l1 = [[32,62],[42,68],[12,98]]
	s1 = [[95,13],[97,25],[93, 37],[79, 27],
		[75, 19],[49, 47],[67, 17]]

	l2 = [[8 ,52],[6 ,80],[26,42],[2 ,72]]
	s2 = [[51, 19],[39, 11],[37, 29],[81, 3],[59, 5],
	  [79, 23],[53, 7],[43, 33],[77, 21]] 
	
	l3 = [[3,54],[37,100]]
	s3 = [[56,33]]

	l4 = [[3,57],[8,100]]
	s4 = [[88,44]]

	l5 = [[3,90]]
	s5 = [[99,10],[97,20],[98,30],[96,40],[95,50],[94,60],[93,70]]

	# print(sol(l3,s3))
	# print(sol(l1,s1))
	# print(sol(l2,s2))

	print(sol(l5,s5))
	
	
