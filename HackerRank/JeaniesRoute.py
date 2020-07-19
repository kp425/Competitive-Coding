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

	def get_weight(self,vertex,nbor):
		return self.edges[vertex][nbor]


def build_graph(edges):
	graph = Graph()
	for i in edges:
		graph.add_edge(*i)
	return graph

def dfs1(graph, start):
	
	visited = set()
	visited.add(start)

	queue = deque([(start,[start],[0])])
	

	while queue:
		vertex_path_distance = queue.pop()
		vertex = vertex_path_distance[0]
		path = vertex_path_distance[1]
		distance = vertex_path_distance[2]
		yield vertex,path,distance

		nbors = graph.get_neighbors(vertex)
		for nbor in nbors:
			if nbor not in visited:
				visited.add(nbor)
				queue.append((nbor,path+[nbor],
					distance+[distance[-1]+graph.get_weight(vertex,nbor)]         ))


def dfs(graph, start):
	
	visited = set()
	visited.add(start)
	queue = deque([(start,[start],0)])
	
	while queue:
		vertex_path_distance = queue.pop()
		vertex = vertex_path_distance[0]
		path = vertex_path_distance[1]
		distance = vertex_path_distance[2]
		yield vertex,path,distance

		nbors = graph.get_neighbors(vertex)
		for nbor in nbors:
			if nbor not in visited:
				visited.add(nbor)
				queue.append((nbor,path+[nbor],
					distance+graph.get_weight(vertex,nbor)))

	


def sol(k, roads):

	roads = roads + [[i[1],i[0],i[2]] for i in roads]
	g = build_graph(roads)
	
	start = 3
	count = 0

	# k.remove(start)

	while True:
		if len(k) == 0:
			break

		for i in dfs(g,start):
			if i[0] in k:
				start = i[0]
				print(i)
				count+=1
				k.remove(i[0])
				break
	
	print("distance :"+str(count))
	
	

	
if __name__ == "__main__":

	k = [1, 3, 4]
	roads = [[1, 2, 1],[2, 3, 2],
			[2, 4, 2],[3, 5, 3]]

	s = sol(k,roads)

	print(s)

	

	
	

	
