
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

k = []
count = -1


def traversal(root):
    global count
    count+= 1

    if len(k)==2:
        return
    if root == None:
        traversal(root.left)
        traversal(root.right)
    if root.left.value > root.value:
        k.append(count)
    
    if root.right.value < root.value:
        k.append(count)


tree_root = None


def __insert(root, val, side):
    if root == None:
        return TreeNode(val)
    if side == "l":
        root.left = __insert(root.left, val, side)
    elif side == "r":
        root.right = __insert(root.right, val, side)
    return root

def insert(val,side):
    global tree_root
    tree_root = __insert(tree_root,val,side)

from collections import deque

def f(l):
    global tree_root
    queue = deque(l)
    while queue:
        item = queue.popleft()
        node = TreeNode(item)
        if tree_root == None:
            tree_root = node
        node.left = TreeNode(queue.popleft())
        node.right = TreeNode(queue.popleft())
        




for i in range(10):
    insert(i)
    
    

print("done")