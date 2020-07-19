from collections import deque


def reverse_string(s):
	ds = deque()
	s_ = ''
	for i in s:
		ds.append(i)

	for i in s:
		s_ += ds.pop()
	return s_

def balanced_string(s):

	match = {"[":"]", "<":">", "(":")"}
	match1 = {"]":"[", ">":"<", ")":"("}

	opposite = match1
	symbol_list = ["[", "(", "<"]
	ds = deque()

	for i in s:

		if i in match.keys():
			ds.append(i)

		if i in match.values():
			if(len(ds) == 0):
				return False
			top = ds.pop()

	return len(ds) == 0


class stack:
	def __init__(self):
		self.ds = deque()

	def push(self, value):
		#Arranging the elements in descending order
		if (len(self.ds) == 0 or self.ds[-1] > value):
			self.ds.append(value)

		elif (self.ds[-1] < value):
			v = self.ds.pop()
			self.ds.append(value)
			self.ds.append(v)

	def pop(self):
		return self.ds.pop()

	def __str__(self):
		return self.ds


class stack_using_array:

	def __init__(self):
		self.ds = []

	def push(self, value):
		self.ds.append(value)

	def pop(self):
		self.ds.pop()

	def __str__(self):
		return self.ds






if __name__ == "__main__":

    

    a = stack_using_array()

    l = [10,7,6,9,1,3,2]

    for i in l:
    	a.push(i)

    a.pop()
    a.pop()
    print(a.__str__())













