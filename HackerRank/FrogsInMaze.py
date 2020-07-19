from collections import deque

class Vertex:
	def __init__(self):
		self.data = None


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


def build_graph(edges):
	graph = Graph()
	for i in edges:
		i.append(6)
		graph.add_edge(*i)
	return graph

def bfs(graph, start):
	
	distance = 0
	visited = set([start])
	queue = deque([(start,distance)])

	while queue:
		vertex_and_distance = queue.popleft()
		yield vertex_and_distance
		for nbor in graph.get_neighbors(vertex_and_distance[0]):
			if nbor not in visited:
				visited.add(nbor)
				distance+=1
				queue.append((nbor,distance))



# -> obstacle, *-> Bomb, O-> Free, % -> Exit






def sol():
	edges1 = [[1,2],[2,3],[3,4],[1,5]]
	edges1 = edges1 + [[i[1],i[0]] for i in edges1]
	edges2 = []

	g = build_graph(edges1)
	l=[]
	for i in bfs(g,1):
		l.append((i[0],i[1]))

	return l
	
if __name__ == "__main__":
	print(sol())
