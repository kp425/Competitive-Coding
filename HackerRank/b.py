
class node:
    def __init__(self, data):
        self.data = data
        self.__edges = []

    def add_edge(self, node_no):
        self.__edges.append(node_no)

    def delete_edge(self, node_no):
        self.__edges.remove(node_no)

    def get_edges(self):
        return self.__edges

class Graph():

    def __init__(self):
        self.nodes = {}
    
    def create(self, c, edges):
        for i,j in enumerate(c):
            self.nodes[i+1]= node(j)
        for i in edges:
            self.nodes[i[0]].add_edge(i[1])

    def __get_sum(self, root_no, s):
        root = self.nodes[root_no]
        root_data = root.data
        s+=root_data
        for i in root.get_edges():
            s = self.__get_sum(i,s)   
        return s
    
    def get_sum(self, root_no):
        my_sum = self.__get_sum(root_no,0)
        return my_sum

    def get_node(self, node_no):
        return self.nodes[node_no]

    


    


    
if __name__ == "__main__":

    #t = BinarySearchTree()
    

    c = [1,2,2,1,1] # add a number 
    edges = [[1,2],[1,3],[3,5],[1,4]] # add a link
    edges = [[1,2],[3,5]]

    c = [15,12,8,14,13]
    edges = [[1,2],[1,3],[4,5],[1,4]]
    #edges = [[1,2],[4,5]]

    t = Graph()
    t.create(c,edges)


    t.nodes[x] = node(value)
    nodes[x].add_edge(y)


    nodes[x1].delete_edge(y1)
    nodes[x2].delete_edge(y2)

    s1 = get_sum(y1)
    s2 = get_sum(y2)
    s3 = get_sum(1)

    if s1 == s2 and s2 == s3:



    
    # t= Tree()
    # nodes[1].delete_edge(3)
    # nodes[1].delete_edge(4)

    # print(get_sum(1))
    # print(get_sum(3))
    # print(get_sum(4))

    
    # print("done")

    

    



        




    #then somehow cut them

    # then add them






# def create(c, edges):
#     for i,j in enumerate(c):
#         nodes[i+1]= node(j)
#     for i in edges:
#         nodes[i[0]].add_edge(i[1])

# def __get_sum(root_no, s):
#     root = nodes[root_no]
#     root_data = root.data
#     s+=root_data
#     for i in root.get_edges():
#         s = __get_sum(i,s)   
#     return s


# def get_sum(root_no):
#     my_sum = __get_sum(root_no,0)
#     return my_sum


    
