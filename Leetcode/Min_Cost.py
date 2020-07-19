
arrows = {4:(-1,0),3:(1,0),2:(0,-1),1:(0,1)}

grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]


def is_valid(grid, index):
	if index[0]<0 or index[1]<0 \
		or index[0]>= len(grid) or index[1]>=len(grid[0]) :
		return False
	return True

from collections import deque

def bfs(grid):
    arrows = {4:(-1,0),3:(1,0),2:(0,-1),1:(0,1)}
    visited = set()
    queue = deque([[(0,0),0]])

    while queue:
        item = queue.popleft()
        current_index = item[0]
        cost = item[1]

        if not is_valid(current_index):
            for i in arrows:
                if i != grid[current_index[0]][current_index[1]]
                    


        nbors = 

        for nbor in nbors:
            visited.add(nbor)
            queue.append((nbor,cost+1))
    