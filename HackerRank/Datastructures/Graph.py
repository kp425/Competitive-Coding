from collections import deque
import heapq




class Graph:

	class Vertex:
		def __init__(self):
			self.visited = False

	def __init__(self):
		self.vertices = {}  #{"1":Vertex(1),"2":Vertex(2)}
		self.edges = {}     #{"1":{2:10,3:20},.....}
								
	def add_vertex(self, vertex):
		self.vertices[vertex] = self.Vertex()

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
	


def build_graph(vertices, edges):
	g = Graph()
	for i in vertices:
		g.add_vertex(i)
	for i in edges:
		g.add_edge(*i)
	return g			

def g1():
	labels = ["s","a","b","c","d","e","f","g"]
	edges = [	["s","a"],["s","b"],["s","c"],
				["a","d"],["a","s"],
				["b","s"],["b","e"],
				["c","s"],["c","f"],
				["d","g"],["d","a"],
				["e","g"],["e","b"],
				["f","g"],["f","c"],
				["g","d"],["g","e"],["g","f"]]
	return build_graph(labels,edges)

def g2():
	v = "abcdef"
	e = "abacbdbcbeceeddfef"
	v = [x for x in v]
	e = list(map(lambda x: [x[0],x[1]],[e[i:i+2] for i in range(0,len(e),2)]))
	e = e+[[i[1],i[0]] for i in e]
	return build_graph(v,e)

def g3():
	v = "abcdefg"
	e = "ab2ac3bd1bc1be4cf5ef1fg1"
	v = [x for x in v]
	e = list(map(lambda x: [x[0],x[1],int(x[2])],[e[i:i+3] for i in range(0,len(e),3)]))
	e = e+[[i[1],i[0],i[2]] for i in e]
	return build_graph(v,e)

def prim(graph,start):

	visited = set()
	visited.add(start)
	queue = deque([start])
	mst = {}
	# for nbor in graph.get_neighbors(start)
	while queue:
		vertex = queue.popleft()
		edges_with_weights = graph.edges[vertex]
		min_weight = min(edges_with_weights.values()) 
		for nbor in edges_with_weights:
			weight = edges_with_weights[nbor]
			if weight==min_weight and nbor not in visited:
				visited.add(nbor)
				queue.append(nbor)
				mst[vertex] = nbor

	return mst




	
	
	


if __name__ == "__main__":

	# d = {"a":1, "b":1}

	# print(min(d,key = d.get))

	g = g3()

	k = prim(g,"a")




	print("done")
	