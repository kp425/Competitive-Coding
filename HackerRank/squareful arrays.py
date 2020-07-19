import math
from itertools import permutations

class Node:
	def __init__(self, data):
		self.parent = None
		self.rank = None
		self.data = data
		# self.size = None
	

class DisjointSet:

	def __init__(self):
		self.ds = {}
		self.no_of_sets = 0

	def make_set(self,u):
		node = Node(u)
		node.rank = 0
		node.parent = u
		self.ds[u] = node
		self.no_of_sets += 1
	
	def union(self,u,v):
		u = self.find_set(u)
		v = self.find_set(v)
		if u == v:
			self.no_of_sets -= 1
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

	def find_set_naive(self,u):
		if self.ds[u].parent == u:
			return parent
		return self.find_set_naive(parent)
	
	#with path compression
	def find_set(self,u):
		parent = self.ds[u].parent
		if parent != u:
			self.ds[u].parent = self.find_set(parent)
		return parent

	def get_node(self,u):
		return self.ds[u]

def isPerfectSquare(a,b):
	sr = math.sqrt(a+b) 
	return (sr - math.floor(sr)) == 0

def isSquaredArray(l):
	if len(l)==0 or len(l)==1:
		return False
	for i in range(0,len(l)-1):
		if not isPerfectSquare(l[i],l[i+1]):
			return False
	return True

def sol(l):
	count = 0
	k = set(permutations(l))
	for i in k:
		if isSquaredArray(i):
			count+=1
	return count



if __name__ == "__main__":
	pass
	
	


	
	
