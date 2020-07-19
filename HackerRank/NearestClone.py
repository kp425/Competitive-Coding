from collections import deque
import os

class Vertex:
	def __init__(self, color):
		self.color = color

class Graph:

	def __init__(self):
		self.vertices = {}  #{"1":Vertex(1),"2":Vertex(2)}
		self.edges = {}     #{"1":{2:10,3:20},.....}
								
	def add_vertex(self, vertex, color):
		self.vertices[vertex] = Vertex(color)

	def add_edge(self, frm, to, weight= 0):
		if frm not in self.edges:
			self.edges[frm] = {}
		self.edges[frm][to] = weight
	
	def get_neighbors(self, vertex):
		return self.edges[vertex].keys()

	def get_vertex(self,vertex):
		return self.vertices[vertex]

def build_graph(vertices,edges,colors):
	graph = Graph()
	for i,j in  zip(sorted(vertices),colors):
		graph.add_vertex(i,j)
	for i in edges:
		i.append(1)
		graph.add_edge(*i)
	return graph

def find_start_1(graph, color):
  
	visited = set()
	queue = deque([1])
	while queue:
		vertex_label = queue.popleft()
		vertex = graph.get_vertex(vertex_label)
		if vertex.color == color:
			return vertex_label
		for neighbor in graph.get_neighbors(vertex_label):
			visited.add(neighbor)
			queue.append(neighbor)
	return -1
		
def find_start(graph, color):
	for key,value in graph.vertices.items():
		if value.color == color:
			return key
	return -1
		


def bfs(graph, start, color):

	# keep adding weigths to get distane
	# objective : compare colors of vertices 

	visited = set()
	queue = deque([start])
	visited.add(start)
	distance = -1
	while queue:
		vertex = queue.popleft()
		if graph.get_vertex(vertex).color == color and vertex!=start:
			return distance
		for neighbor in graph.get_neighbors(vertex):
			if neighbor not in visited:
				visited.add(neighbor)
				queue.append(neighbor)
		distance+=1
	return -1

def g1():
	vertices = [1,2,3,4]
	edges = [[1,2],[1,3],
			 [2,1],[2,4],[3,1],[4,2]]
	colors = [1,2,1,1]
	
	return build_graph(vertices,edges,colors)

def g2():
	g_from = [1,1,4]
	g_to = [2,3,2]
	ids = [1,2,3,4]
	val = 2
	init(g_from, g_to, ids, val)

def g3():
	g_from = [1,1,2,3]
	g_to = [2,3,4,5]
	ids = [1,2,3,3,2]
	val = 2
	init(g_from, g_to, ids, val)

def g4():
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')

	fptr = open("/Users/KP/Desktop/NearestClone.txt","w")

	graph_nodes, graph_edges = map(int, input().split())

	graph_from = [0] * graph_edges
	graph_to = [0] * graph_edges

	for i in range(graph_edges):
		graph_from[i], graph_to[i] = map(int, input().split())

	ids = list(map(int, input().rstrip().split()))

	val = int(input())

	ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

	fptr.write(str(ans) + '\n')

	fptr.close()

	return init(graph_from,graph_to, ids, val)


def init(graph_from, graph_to, ids, val):

	edges = []
	nodes = set()
	for i,j in zip(graph_from, graph_to):
		nodes.add(i)
		nodes.add(j)
		edges.append([i,j]) 
		edges.append([j,i])
	
	g = build_graph(nodes,edges,ids)
	start = find_start(g,val)
	d = bfs(g,start,val)
	print(d)
	return d
 




if __name__ == "__main__":
	
	g4()
	# g = g1()
	# color = 1
	# start = find_start(g,color)
	# d = bfs(g,start,1)
	# print(d)
	# print("done")