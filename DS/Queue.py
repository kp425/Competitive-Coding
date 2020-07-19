from collections import deque
import unittest

def reverse_queue(q):
	stack = deque()
	while(len(q)!= 0):
		stack.append(q.popleft())

	while(len(stack)!= 0):
		q.append(stack.pop())
	return q

class queue_with_list:
	def __init__(self):
		self.queue = []
		self.first = None
		self.last = None
	def enqueue(self, value):
		if(len(self.queue)==0):
			self.first = value
		self.last += 1
		self.queue.append(value)
	
	def dequeue(self):
		pass
	def is_empty(self):
		pass
	def is_full(self):
		pass
	def peek(self):
		pass

class test_queue_functions(unittest.TestCase):
	
	def test_reverse_queue(self):
		q1 = deque([10,20,30])
		q2 = deque([])
		q3 = deque([1])
		q4 = deque([10,20])
		self.assertEqual(reverse_queue(q1), deque([30,20,10]))
		self.assertEqual(reverse_queue(q2), deque([]))
		self.assertEqual(reverse_queue(q3), deque([1]))
		self.assertEqual(reverse_queue(q4), deque([20,10]))



if __name__ == "__main__":
	
	unittest.main()
	print(reverse_queue(deque([10,20,30]))) 

	 



	







