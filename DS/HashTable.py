class hashTable:

	def __init__(self):
		self.table = []

	def put(k,v):
		index = hashFunction(k)
		data = pair(k,v)
		if (self.table[index]== None):
			self.table[index] = linkedList()
		ll = self.table[index]
		temp_node = ll.head
		for i in range(0,ll.size):
			if(temp_node.value == value):
				temp_node.data = node(value)

			else:
				temp_node = temp_node.next

		self.table[index].append(data)

		

		

	def get(k):
		return self.d[k]

	def remove(k):
		pass

	def hashFunction(k):
		return k%5


class pair:
	def __init__(self, k, v):
		self.k = k
		self.v = v

class node:
	def __init__(self, value):
		self.value = value
		self.next = None
	def getValue(self):
		return self.value
	def getNext(self):
		return self.next
	def setValue(self, value):
		self.value = value
	def setNext(self, next):
		self.next = next

class linkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def append(self, value):
		if (self.size == 0):
			self.head = node(value)
				
		else:
			temp_node = self.head
			for i in range(0,self.size):
				if(temp_node.next!=None):
					temp_node = temp_node.next
				else:
					temp_node.next = node(value)
			
		self.size+=1

	
	def doesValueExists(self, value):

		temp_node = self.head
		for i in range(0, self.size):
			if(temp_node.value == value):
				return True
		return False



	def printAll(self):
		temp_node = self.head
		for i in range(0, self.size):
			print(temp_node.value)
			temp_node = temp_node.next

		
			




l = linkedList()

l.printAll()


h = hashTable()





