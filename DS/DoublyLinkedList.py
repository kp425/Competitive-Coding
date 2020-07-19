class DoublyLinkedList:

    class Node:
        def __init__(self, value):
            self.value = value
            self.next_node = None
            self.prev_node = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

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
        pass

    



    