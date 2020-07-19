import unittest

class Node:
    def __init__(self, value = None):
        self.value = value
        self.__children = {}
        self.isWordFinished = False

    def hasChild(self, char):
        return char in self.__children

    def addChild(self, char):
        self.__children[char] = Node(char)

    def getChild(self, char):
        return self.__children[char]

    def getChildren(self):
        return self.__children.values()
        #return self.__children
    
    



class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        current = self.root
        for i in string:
            if(not current.hasChild(i)):
                current.addChild(i)
            current = current.getChild(i)
        current.isWordFinished = True

    def contains(self, string):
        if(string == None):
            return False
        current = self.root
        length = len(string)
        for i in range(0,length):
            char = string[i]
            if(not current.hasChild(char)):
                return False
            current = current.getChild(char)     
        return current.isWordFinished

    def __traverse_preorder(self, node):
        print(node.value)
        for i in node.getChildren():
            self.__traverse_preorder(i)


    def __traverse_postorder(self, node):
        for i in node.getChildren():
            self.__traverse_postorder(i)
        print(node.value)

    def traverse_preorder(self):
        self.__traverse_preorder(self.root)
    
    def traverse_postorder(self):
        self.__traverse_postorder(self.root)

    def remove_word(self, string):
        current = self.root
        for i in string:
            current = current.getChild(i)
        current.isWordFinished = False
        if (not current.hasChildren()):
            pass
            #current.
    
    def __remove_word(self, node, string, index):

        if(index == len(word)):
            pass
            
        
        char = string[index]
        child = node.getChild(char)
        if(child == None):
            return
        self.__remove_word(child, word, index+1)

        

            






if __name__ == "__main__":

    # insert_words = ["cat", "can", "fruit", "ca", "lichess", "chess"]

    # test_dict = ["ca", "cat", "sex", "z","canfood"]

    ds = Trie()

    for i in ["canr", "canada", "sex"]:
        ds.insert(i)
    
    ds.traverse_postorder()

    


  
         
