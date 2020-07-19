from collections import deque

class Vertex:
	def __init__(self,**kwargs):
		for key,value in kwargs:
			setattr(self,key,value)


class Graph:

	def __init__(self):
		self.vertices = {}  #{"1":Vertex(1),"2":Vertex(2)}
		self.edges = {}     #{"1":{2:10,3:20},.....}
							
	def add_vertex(self, vertex, **kwargs):
		self.vertices[vertex] = Vertex(kwargs)

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

def isSatisfied(ca,cp,ha,hp):
	return ha>=ca and hp<=cp


def build_graph(vertices,edges):
	graph = Graph()
	for i in vertices: 
		graph.add_vertex(i)
	for i in edges:
		i.append(-1)
		graph.add_edge(*i)
	return graph

def sol(clients, houses):
	g = build_graph(clients,houses)

def parse_tests(string):
	string_split = string.split(" ")
	string_list= [[int(string_split[i]),int(string_split[i+1])] \
					for i in range(0,len(string_split)-1,2)]
	no_c = string_list[0][0]
	c = string_list[1:no_c+1]
	h = string_list[no_c+1:]
	return c,h

if __name__ == "__main__":
	string = "3 3 5 110 9 500 20 400 10 100 2 200 30 300"
	c,h = parse_tests(string)
	k = sol(c,h)
	print(k)

	

	