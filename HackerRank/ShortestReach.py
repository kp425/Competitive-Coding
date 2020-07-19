from collections import deque

class Vertex:
	def __init__(self):
		self.visited = False


class Graph:

	def __init__(self):
		self.vertices = {}  #{"1":Vertex(1),"2":Vertex(2)}
		self.edges = {}     #{"1":{2:10,3:20},.....}
							
		
	def add_vertex(self, vertex):
		self.vertices[vertex] = Vertex()

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


def build_graph(vertices,edges):
	graph = Graph()
	for i in vertices:
		graph.add_vertex(i)
	for i in edges:
		i.append(-1)
		graph.add_edge(*i)
	return graph

def bfs_1(graph, start):
	distance = 0
	visited = set([start])
	queue = deque([(start,distance)])
	while queue:
		vertex_and_distance = queue.popleft()
		vertex = vertex_and_distance[0]
		distance = vertex_and_distance[1]
		yield vertex_and_distance
		nbors = graph.get_neighbors(vertex)
		for nbor in nbors:
			if nbor not in visited:
				visited.add(nbor)
				queue.append((nbor,distance+1))
				# graph.edges[vertex][nbor] = 6*(distance+1)

# def bfs(graph, start):
# 	distance = 0
# 	visited = set([start])
# 	queue = deque([start])
# 	while queue:
# 		vertex = queue.popleft()
# 		nbors = graph.get_neighbors(vertex)
# 		for nbor in nbors:
# 			if nbor not in visited:
# 				visited.add(nbor)
# 				queue.append(nbor)
# 				graph.edges[vertex][nbor] = 6*(distance+1)
		
		
def sol(n, m, edges, s):
	# edges_ = [[1,2],[1,3],[3,4]]
	# edges = edges_ + [[i[1],i[0]] for i in edges_]

	edges_ = edges
	edges = edges_ + [[i[1],i[0]] for i in edges_]
	g = build_graph([i for i in range(1,n+1)],edges)

	l = []
	for i in bfs_1(g,s):
		if i[0]!=s:
			l.append((i[0],6*i[1]))

	for i in range(1,n+1):
		if i not in g.edges:
			l.append((i,-1))
	
	
	for i in sorted(l):
		print(i)
	return [i[1] for i in sorted(l)]


	
	
if __name__ == "__main__":
	edges = [[3,1],[10,1],[10,1],[3,1],[1,8],[5,2]]

	k = sol(10,6,edges,3)

	print(k)
	




