from collections import defaultdict, deque

def build_graph(numCourses,prerequisites):
    d = defaultdict(list)
    for i in range(numCourses):
        d[i] = []
    for i in prerequisites:
        if i[1] in d:
            if i[0] in d[i[1]]:
                return None
        d[i[0]].append(i[1])
    return d
        
def sol(numCourses,prerequisites):
    g = build_graph(numCourses, prerequisites)
    if g == None:
        return False
    if prerequisites==[]:
        return True
    for i in prerequisites:
        if dfs(g,i[0],i[1]) == False:
            return False
    return True



def dfs(graph,start,end):
    visited = set()
    visited.add(start)
    queue = deque([start])
    while queue:
        item = queue.pop()
        nbors = graph[item]
        for nbor in nbors:
            if nbor == end:
                return True
            if nbor in visited:
                return False
            visited.add(nbor)
            queue.append(nbor)
    return False



numCourses = 2 #True
prerequisites = [[1,0]]

numCourses = 2 #False
prerequisites = [[1,0],[0,1]]

numCourses = 3 #False
prerequisites = [[1,0],[0,2],[2,1]]

# numCourses = 3 #True
# prerequisites = [[2,0],[2,1]]

# numCourses = 3 #True
# prerequisites = [[0,1],[0,2],[1,2]]


k  = sol(numCourses,prerequisites)

print(k)