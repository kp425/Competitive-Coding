class Node:
	def __init__(self):
		self.parent = None
		self.rank = 0
		self.size = 0
		self.count = 0
		# self.size = None
	
class DisjointSet:

	def __init__(self):
		self.ds = {}
		self.no_of_sets = 0
		self.cache = []

		
	def make_set(self,u):
		node = Node()
		node.parent = u
		node.size+=1
		self.ds[u] = node
		self.no_of_sets += 1
	
	def union(self,ul,vl):
		if ul==vl:
			pass
		u = self.find_set(ul)
		v = self.find_set(vl)
		if u == v:
			node_u = self.ds[u]
			# node_u.size +=1
			# node_u.count += 1
			self.cache.append(node_u.count*node_u.size)
			return

		node_u = self.ds[u]
		node_v = self.ds[v]
		node_u_rank = node_u.rank
		node_v_rank = node_v.rank

		if node_u_rank >= node_v_rank:
			if node_u_rank == node_v_rank: 
				node_u.rank = node_u_rank+1
			node_v.parent = u
			node_u.size += node_v.size
			node_u.count += 1
			self.cache.append(node_u.count*node_u.size)
			
		else:
			node_u.parent = v
			node_v.size += node_u.size
			node_v.count+= 1
			self.cache.append(node_v.count*node_v.size)
		self.no_of_sets -= 1
	
	#with path compression
	def find_set(self,u):
		parent = self.ds[u].parent
		if parent != u:
			self.ds[u].parent = self.find_set(parent)
		return parent

	def get_node(self,u):
		return self.ds[u]


def sol(n,friendships):

	d = DisjointSet()

	for i in range(n):
		d.make_set(i)
	
	for i in friendships:
		d.union(*i)

	return sum(d.cache)

if __name__ == "__main__":

	n = 5
	edges = [[1,2],[3,2],[4,2],[4,3]]

	print(sol(n,edges))