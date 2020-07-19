# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	

class Codec:
	def serialize(self, root):
		def _serialize(root, l= []):
			if root:
				l.append(root.val)
				_serialize(root.left,l)
				_serialize(root.right,l)
			else:
				l.append("null")
			return l	
		return str(_serialize(root))

	def deserialize(self, data):
		data = list(data)
		def _deserialize(root, data):
			val = data[0]
			if root == None and val!="null":
				return TreeNode(val)
			if root == None and val == "null":
				return None
			root.left = _deserialize(root.left,data[1:])
			root.right = _deserialize(root.right,data[1:])
			return root
		
		root = _deserialize(None, data)
		return root


def build():	
	t1 = TreeNode(1)
	t2 = TreeNode(2)
	t3 = TreeNode(3)
	t4 = TreeNode(4)
	t5 = TreeNode(5)
	t1.left = t2
	t1.right = t3
	t3.left = t4
	t3.right = t5
	return t1
tree = build()
codec = Codec()
k = codec.serialize(tree)
print(k)
r = codec.deserialize(k)
print("Done")





# class Tree:
#     def __init__(self):
#         self.root = None
	
#     def insert(self, val):
#         self.root = self.__insert(self.root, val)

#     def __insert(self, root, val):
#         if root == None:
#             return TreeNode(val)
#         root.left = self.__insert(root.left, val)
#         root.right = self.__insert(root.right, val)
		
# t = Tree()
# for i in range(10):
#     t.insert(i)
# print("done")