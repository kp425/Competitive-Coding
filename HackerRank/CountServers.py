

from collections import deque

visited = set()

def get_neighbors(index):
	l = []
	offsets = [(0,-1),(-1,0),(1,0),(0,1)]
	return list(map(lambda x: (x[0]+index[0],x[1]+index[1]), offsets))

def isQualified(grid,index):
	no_row = len(grid)
	no_col = len(grid[0])
	if index[0]<0 or index[1]<0  \
		or index[0]>no_row-1 or index[1]> no_col-1:
		return False
	if grid[index[0]][index[1]] == 0:
		return False
	return True

def dfs(grid,start):

	if not isQualified(grid,start) or start in visited:
		return 0
	else:
		visited.add(start)
		queue = deque([start])
		count = 1
		while queue:
			vertex = queue.pop()
			nbors = get_neighbors(vertex)
			for nbor in nbors:
				if nbor not in visited and isQualified(grid,nbor):
					count+=1
					visited.add(nbor)
					queue.append(nbor)
	if count==1:
		return 0
	return count

def sol(grid):
	s = 0
	no_row = len(grid)
	no_col = len(grid[0])
	for i in range(no_row):
		for j in range(no_col):
			s+=dfs(grid,(i,j))
	return s
		

grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]




		
			







