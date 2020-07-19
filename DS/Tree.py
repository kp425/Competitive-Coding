import Queue

class Node:

	def __init__(self, value):
		self.value = value
		self.lChild = None
		self.rChild = None

class Tree:

	def __init__(self, *args):
		self.root = None


	def find(self, value):
		temp_node = self.root
		
		while(temp_node != None):

			if(value < temp_node.value):
				temp_node = temp_node.lChild

			elif(value > temp_node.value):	
				temp_node = temp_node.rChild
			
			elif (value == temp_node.value):
				return True

		return False
		
		

	def insert(self, value):

		node = Node(value)
		if(self.root == None):
			self.root = node
		else:
			temp_node = self.root
			while (True):
				if(value < temp_node.value):
					if(temp_node.lChild == None):
						temp_node.lChild = node
						break	
					else:
						temp_node = temp_node.lChild
							
				elif(value > temp_node.value):	
					if(temp_node.rChild == None):
						temp_node.rChild = node
						break	
					else:
						temp_node = temp_node.rChild


	def traversePreOrder(self, root):
		if(root == None):
			return
		print(root.value)
		self.traversePreOrder(root.lChild)
		self.traversePreOrder(root.rChild)
	
	def traverseInOrder(self, root):
		if(root == None):
			return
		self.traverseInOrder(root.lChild)
		print(root.value)
		self.traverseInOrder(root.rChild)
	
	def traversePostOrder(self, root):
		if(root == None):
			return
		self.traversePostOrder(root.lChild)
		self.traversePostOrder(root.rChild)
		print(root.value)

	def Height(self, node):
		if(node.lChild == None and node.rChild == None):
			return 0

		return 1 + max(self.Height(node.lChild),
					 self.Height(node.rChild))
		

		
		
		
		

			


	def printAll(self):

		q = Queue.Queue()
		temp_node = self.root
		q.add(temp_node)
		level = 0

		while(level < 6):
			if (level==0):
				node = q.remove()
				print(node.value)
				q.add(node.lChild)
				q.add(node.rChild)
				level += 1
			else:
				for i in range(2*level):
					node = q.remove()
					if(node.value != None):
						print(node.value)
					else:
						print("N")
					
					q.add(node.lChild)
					q.add(node.rChild)
				level+=1	

	def Delete(self, index):
		pass

	def append(self):
		pass

	def Remove(self):
		pass

	def __repr__(self):
		pass





if __name__ == "__main__":

	l1 = [8, 10, 1, 12, 15, 17, 6, 5, 18]
	l = [7,4,9,1,6,8,10]
	t = Tree()

	for i in l:
		t.insert(i)

	# print(t.find(8))
	# print(t.find(10))
	# print(t.find(6))
	# print(t.find(17))
	# print(t.find(20))
	# print(t.find(42))
	# print(t.find(0))
	# print(t.find(13))



	print(t.Height(t.root))




	




