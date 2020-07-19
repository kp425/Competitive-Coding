# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]

from collections import deque

info = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        info[(i,j)] = False


def is_valid(grid, index):
	if index[0]<0 or index[1]<0 \
		or index[0]>= len(grid) or index[1]>=len(grid[0]) :
		return False,index
	return True,index

 

def get_next(grid, index, val = None):
    x,y = index[0],index[1]
    if val == None:
        val = grid[x][y]
    next_ = None
    if val == 1:
        next_ = is_valid(grid,(x,y+1))
    elif val == 2:
        next_ = is_valid(grid,(x,y-1))
    elif val == 3:
        next_ = is_valid(grid,(x+1,y))
    elif val == 4:
        next_ = is_valid(grid,(x-1,y))
    
    return next_[0],next_[1],val


# print(get_next(grid,(0,3)))

def bfs(grid):
    f = []
    vals = [1,2,3,4]
    visited = set()
    visited.add((0,0))
    queue = deque([[(0,0),0]])
    
    while queue:
        item = queue.popleft()
        if item[0] == (len(grid)-1,len(grid[0])-1):
            f.append(item)
        
        next_ = get_next(grid,item[0])
        nbors = []
        if next_[0] == False:
            for val in vals:
                if next_[2]!=val:
                    _ = get_next(grid,next_[1],val)[1]
                    nbors.append(_)
        else:
            nbors.append(next_[1])
            
        for nbor in nbors:
            if nbor not in visited:
                visited.add(nbor)
                queue.append([nbor,item[1]+1])
    return f


k = bfs(grid)

print(k)