grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]

grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]


def is_qualified(grid, index):
	if index[0]<0 or index[1]<0 \
		or index[0]>= len(grid) or index[1]>=len(grid[0]) :
		return False
	return True

def get_nbors(grid, index):
	offsets = [[-1,0],[1,0],[0,1],[0,-1]]
	l = [(index[0]+x[0],index[1]+x[1]) for x in offsets]
	return [i for i in l if is_qualified(grid,i)]

from collections import deque

def bfs(grid,start):

    visited = set()
    queue = deque([start])

    while queue:

        item = queue.pop()
        
