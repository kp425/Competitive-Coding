
class Node:
	def __init__(self):
		self.parent = None
		self.rank = 0
		self.size = 0
		# self.size = None
	
class DisjointSet:

	def __init__(self):
		self.ds = {}
		self.no_of_sets = 0
		self.cache = {}
		
	def make_set(self,u):
		node = Node()
		node.parent = u
		node.size+=1
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
			node_u.size += node_v.size
			node_v.size = 0
			
			self.cache[u] = node_u.size
			self.cache.pop(v,None)
			

		else:
			node_u.parent = v
			node_v.size += node_u.size
			node_u.size = 0
			self.cache[v] = node_v.size
			self.cache.pop(u,None)
		self.no_of_sets -= 1
	
	#with path compression
	def find_set(self,u):
		parent = self.ds[u].parent
		if parent != u:
			self.ds[u].parent = self.find_set(parent)
		return parent

	def get_node(self,u):
		return self.ds[u]


def sol(n,astronaut):
	#l = [[0,1],[2,3],[0,4]]
	#s = set([item for sublist in l for item in sublist])
	# import functools
	# import operator
	# s1 = set(functools.reduce(operator.iconcat, astronaut, []))
	
	d = DisjointSet()

	for i in range(n):
		d.make_set(i)
	# d.cache = d.ds.copy()
	for i in astronaut:
		d.union(*i)
	
	f = []
	for i,j in d.ds.items():
		if j.parent==i:
			print(i)
			f.append(j.size)

	s = 0
	for i in range(len(f)):
		for j in range(i+1,len(f)):
			s+= f[i]*f[j]
	return s

def read_test_cases():
	import os
	f = os.path.join(os.path.dirname(__file__), 'JourneyToMoon.txt')
	data = open(f,'r')
	l = []
	for i in data.readlines():
		j = i.strip().split(" ")
		k = [int(j[0]),int(j[1])]
		l.append(k)
	
	return l[0][0],l[1:]


if __name__=="__main__":
	

	a,b = read_test_cases()
	
	# print(sol(5,[[0,1],[2,3],[0,4]]))
	# print(sol(4,[[0,2]]))

	print(sol(a,b))
