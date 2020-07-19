
from collections import deque

def is_qualified(grid, index):
    if index[0]<0 or index[1]<0 \
        or index[0]>= len(grid) or index[1]>=len(grid[0]) \
        or grid[index[0]][index[1]]=="0":
        return False
    return True

def get_nbors(grid, index):
    # offsets = [[-1,0],[1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
    offsets = [[-1,0],[1,0],[0,1],[0,-1]]
    l = [(index[0]+x[0],index[1]+x[1]) for x in offsets]
    return [i for i in l if is_qualified(grid,i)]
    # return filter(lambda x:is_qualified(grid,x),l)


def dfs(grid,start):
    visited = set()
    visited.add((start[0],start[1]))
    stack = deque([start])
    while stack:
        item = stack.pop()
        nbors = get_nbors(grid, item)
        for nbor in nbors:
            if nbor not in visited:
                visited.add(nbor)
                stack.append(nbor)
    return visited


def sol(grid):
    count = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]!="0":
                if (i,j) not in visited:
                    temp_v = dfs(grid,(i,j))
                    visited = visited.union(temp_v)
                    count+=1
    return count
    




def parse_input(s):
    s = s.split()
    l = [list(i) for i in s]
    return l

a = "11110  11010   11000   00000"
b = "11000   11000   00100   00011"

grid = parse_input(a)


grid = [["1"]]


k = sol(grid)
print(k)




