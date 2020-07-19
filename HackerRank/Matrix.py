from collections import deque

class Vertex:
	def __init__(self):
		self.machine = False


class Graph:

	def __init__(self):
		self.vertices = {}  #{"1":Vertex(1),"2":Vertex(2)}
		self.edges = {}     #{"1":{2:10,3:20},.....}
									
	def add_vertex(self, vertex):
		self.vertices[vertex] = Vertex()

	def add_edge(self, frm, to, weight= 0):
		if frm not in self.vertices:
			self.vertices[frm] = Vertex()
		if to not in self.vertices:
			self.vertices[to] = Vertex()
		if frm not in self.edges:
			self.edges[frm] = {}
		self.edges[frm][to] = weight
	
	def get_neighbors(self, vertex):
		return self.edges[vertex].keys()

	def get_vertex(self,vertex):
		return self.vertices[vertex]


def g1():
	roads = [[2,1,8],[1,0,5],[2,4,5],[1,3,4]]
	machines = [2,4,0]
	return build_graph(roads,machines)


def build_graph(roads,machines):
	graph = Graph()
	for i in roads:
		graph.add_edge(*i)
		graph.add_edge(i[1],i[0],i[2])

	for i in machines:
		graph.vertices[i].machine = True
	return graph

def minTime():
	pass

	# get specific edges
	# return sum of weights of those edges

if __name__ == "__main__":
	g = g1()
	print("done")

	

	
