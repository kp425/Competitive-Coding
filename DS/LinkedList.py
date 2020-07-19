import unittest

class SinglyLinkedList:

	class Node:
		def __init__(self, value, next_node = None):
			self.value = value
			self.next_node = next_node

	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0

	def removeFirst(self):
		if(self.head == None):
			return
		else:
			if(self.head == self.tail):
				self.head = self.tail = None
			else:
				self.head = self.head.next_node
			self.count-=1
	

	def removeLast(self):
		current_node = self.head
		while(True):
			if(current_node.next_node != self.tail):
				current_node = current_node.next_node
			else:
				self.tail = current_node
				break
		self.count-=1
	
	def remove(self, value):
		current_node = self.head
		while(True):
			if(current_node.next_node.value != value):
				current_node = current_node.next_node
			else:
				current_node.next_node = current_node.next_node.next_node
		self.count-=1

	def addFirst(self, value):
		node = self.Node(value)
		if(self.head == None):
			self.head = node
		elif(self.count == 1):
			node.next_node = self.tail = self.head
			self.head = node
		else:
			node.next_node = self.head
			self.head = node
		self.count+=1
			
	 

	def addLast(self, value):
		node = self.Node(value)
		if(self.count == 0):
			self.head = node
		elif (self.count == 1):
			self.head.next_node = self.tail = node
		else:
			self.tail.next_node = node
			self.tail = node
		self.count+=1

	
	def print_all(self):
		temp_node = self.head
		for x in range(0,self.count):
			print(temp_node.value)
			if temp_node.next_node != None:
				temp_node = temp_node.next_node

	def reverse(self):
		#1->2->3
		previous = self.head
		current = previous.next_node

		while(current!=None):
			next_ = current.next_node
			current.next_node = previous
			previous = current
			current = next_

		self.tail = self.head
		self.tail.next_node = None
		self.head = previous

	def kth_node_from_end(self, k):

		first_pointer = self.head
		second_pointer = self.head

		for i in range(0, k-1):
			temp = second_pointer.next_node
			second_pointer = temp
		
 
		while(second_pointer!=self.tail):
			first_pointer = first_pointer.next_node
			second_pointer = second_pointer.next_node
		
		return first_pointer.value

	

class TestSinglyLinkedList(unittest TestCase):

	def test_kth_node_from_end(self):
		l1 =  [1,2,3,4,5,6]
		l2 =  []
		l3 =  [1]
		l4 =  [1,2]

		l5 = [10,20,30,40,50]
		
		#ll1 = lambda x:

		#self.assertEqual()

		self.assertEqual()






			

if __name__ == "__main__":
	
	l = SinglyLinkedList()

	a = [1,2,3,4,5,6]
	b = [11,12,13,14,15,16]

	for i in b:
		l.addLast(i)
	
	k = l.kth_node_from_end(2)

	print(k)
	
	print("Done")







