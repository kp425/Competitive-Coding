
class AVLTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.lChild = None
            self.rChild = None
            self.height = 0

    def __init__(self):
        self.root = None
        

    def Insert(self, value):
        self.root = self.__Insert(self.root, value)

    def __Insert(self, root, value):
        
        if(root == None):
            return self.Node(value)

        if(value < root.value):
            root.lChild = self.__Insert(root.lChild, value)
        elif(value > root.value):
            root.rChild = self.__Insert(root.rChild, value)
        root.height = 1 + max(self.__Height(root.lChild), 
                              self.__Height(root.rChild))
        
        self.balance(root)

        return root
    
    def __Height(self, node):
        if(node == None):
            return -1
        else:
            return node.height
        

    def traverseInOrder(self, root):
        if(root == None):
            return
        self.traverseInOrder(root.lChild)
        print(root.value, root.height)
        self.traverseInOrder(root.rChild)
    
    def isLeftHeavy(self, node):
        return self.balanceFactor(node) > 1
    
    def isRightHeavy(self, node):
        return self.balanceFactor(node) < -1

    def balanceFactor(self, node):
        return self.__Height(node.lChild) - self.__Height(node.rChild)

    
    def setHeight(self, node):
        return max(self.__Height(node.lChild), self.__Height(node.rChild)) + 1
    
    def leftRotate(self, root):
        newRoot = root.rChild
        root.rChild = newRoot.lChild
        newRoot.lChild = root
        self.setHeight(root)
        self.setHeight(newRoot)

    def rightRotate(self, root):
        newRoot = root.lChild
        root.lChild = newRoot.rChild
        newRoot.rChild = root
        self.setHeight(root)
        self.setHeight(newRoot)
        

    def balance(self, node):
        if (self.isLeftHeavy(node)):
            if(self.balanceFactor(node.lChild) < 0):
                self.leftRotate(node.lChild)
            self.rightRotate(node)
            
        elif (self.isRightHeavy(node)):
            if(self.balanceFactor(node.rChild) > 0):
                self.rightRotate(node.rChild)
            self.leftRotate(node)







if __name__ == "__main__":

    t = AVLTree()
    t.Insert(10)
    t.Insert(30)
    t.Insert(20)


    t.traverseInOrder(t.root)
    




    