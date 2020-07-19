class Graph:

	class Node:
		def __init__(self, label):
			self.label = label

		def __str__(self):
			return "Node "+str(self.label)

	def __init__(self):
		self.graph_dict = {}

	def find(self, value):
		pass

	def addNode(self, label):
		self.graph_dict[label] = []
		
	def removeNode(self, label):
		self.graph_dict.pop(label, None)

	def addEdge(self, frm, to):
		to_node = self.Node(to)
		self.graph_dict[frm].append(to_node)

	def removeEdge(self, frm, to):
		to_node = self.Node(to)
		self.graph_dict[frm].remove(to_node)






if __name__ == "__main__":
	g = Graph()

	g.addNode(1)
	g.addNode(2)
	g.addNode(3)
	g.addNode(4)

	g.addEdge(1,2)
	g.addEdge(1,3)
	g.addEdge(1,4)
	g.addEdge(2,4)
	g.addEdge(3,4)
	g.addEdge(4,2)


	for value in g.graph_dict.values():
		value.print_all()
		print(" ")



	

