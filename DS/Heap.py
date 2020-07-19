class Heap:

    class Node:
        def __init__(self, value):
            self.value = value
            self.lChild = None
            self.rChild = None

    def __init__(self):
        self.root = None

    def Insert(self, value):
        self.root = self.__Insert(self.root, value)

    def __Insert(self, root, value):
        if (root == None):
            return self.Node(value)

        if(value < root.value):

            
            if(root.lChild != None):
                root.lChild = self.__Insert(root.lChild, value)
            elif(root.rChild != None)
                root.rChild = self.__Insert(root.rChild, value)

        return root

    def __traversePreOrder(self, root):
        if(root == None):
            return
        print(root.value)
        self.__traversePreOrder(root.lChild)
        self.__traversePreOrder(root.rChild)

    def traversePreOrder(self):
        self.__traversePreOrder(self.root)
    
    def bubbleUp(self):
        pass

    def bubbleDown(self):
        pass


if __name__ == "__main__":

    h = Heap()

    h.Insert(10)
    h.Insert(9)
    h.Insert(8)
    # h.Insert(7)
    # h.Insert(6)

    h.traversePreOrder()

    print("done")
    


