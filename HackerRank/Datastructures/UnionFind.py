

class DisjointSet:

	class Node:
		def __init__(self, data):
			self.parent = None
			self.rank = None
			self.data = data
			# self.size = None

	def __init__(self):
		self.ds = {}
		self.no_of_sets = 0

	def make_set(self,u):
		node = self.Node(u)
		node.rank = 0
		node.parent = u
		self.ds[u] = node
		self.no_of_sets += 1
	
	def union(self,u,v):
		u = self.find_set(u)
		v = self.find_set(v)
		if u == v:
			return

		node_u = self.ds[u]
		node_v = self.ds[v]
		node_u_rank = node_u.rank
		node_v_rank = node_v.rank

		if node_u_rank >= node_v_rank:
			if node_u_rank == node_v_rank: 
				node_u.rank = node_u_rank+1
			node_v.parent = u
		else:
			node_u.parent = v
		self.no_of_sets -= 1
	
	#with path compression
	def find_set(self,u):
		parent = self.ds[u].parent
		if parent != u:
			self.ds[u].parent = self.find_set(parent)
		return parent

	def get_node(self,u):
		return self.ds[u]




	





			