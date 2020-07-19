
class Node:
	def __init__(self, data):
		self.parent = None
		self.rank = None
		self.data = data
		self.size = 1

	def get_parent(self):
		return self.parent
	def get_rank(self):
		return self.rank
	def get_data(self):
		return self.data

	def set_parent(self,parent):
		self.parent = parent
	def set_rank(self,rank):
		self.rank = rank
	def set_data(self,data):
		self.data = data


class DisjointSet:

	def __init__(self):
		self.ds = {}
		self.no_of_sets = 0
		self.max_size = 1


	def make_set(self,u):
		node = Node(u)
		node.set_rank(0)
		node.set_parent(u)
		self.ds[u] = node
		self.no_of_sets += 1
	
	def update_max_size(self, node_u):
		if node_u.size > self.max_size:
			self.max_size = node_u.size

	
	def union(self,u,v):
		u = self.find_set(u)
		v = self.find_set(v)
		if u == v:
			return

		node_u = self.get_node(u)
		node_v = self.get_node(v)
		node_u_rank = node_u.get_rank()
		node_v_rank = node_v.get_rank()

		if node_u_rank >= node_v_rank:
			if node_u_rank == node_v_rank: 
				node_u.set_rank(node_u_rank+1)
			node_v.set_parent(u)
			node_u.size +=1
			self.update_max_size(node_u)

		else:
			node_u.set_parent(v)
			node_v.size +=1
			self.update_max_size(node_v)
		self.no_of_sets -= 1

	def find_set(self,u):
		node = self.get_node(u)
		parent = node.get_parent()
		if parent == u:
			return parent
		return self.find_set(parent)

	def get_node(self,u):
		return self.ds[u]


if __name__ == "__main__":

	d = DisjointSet()

	l = []
	k = sorted(l)

	for i in k:
		d.make_set(i)
	
	for i in range(len(k)-1):
		if k[i]+1 == k[i+1]:
			d.union(k[i],k[i+1])
	
	print(d.max_size)

	


	





	# for i in l:
	#     d.make_set(i)


	
	
	

	