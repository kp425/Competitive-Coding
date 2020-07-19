board = [[1,2,3],
		[4,0,5]]

board = [[1,2,3],[5,4,0]]
board = [[4,1,2],[5,0,3]]
board = [[3,2,4],[1,5,0]]

from collections import deque

def is_qualified(grid, index):
	if index<0 or index>= len(grid):
		return False
	return True

def get_nbors(grid, index):
	if index == 2:
		offsets = [-1,-3,3]
	elif index == 3:
		offsets = [1,-3,3]
	else:
		offsets = [-1,-3,1,3]
	l = [index+x for x in offsets]
	return [i for i in l if is_qualified(grid,i)]

def swap(grid,index1,index2):
	if index1 > index2:
		temp = index1
		index1 = index2
		index2 = temp
	return grid[:index1] + grid[index2]+ \
		grid[index1+1:index2] + grid[index1]+grid[index2+1:]


def sol(board):
	string = "".join(map(str,sum(board,[])))
	return bfs(string)



def bfs(string):

	visited = set()
	visited.add(string)
	queue = deque([(string,0)])
	
	while queue:
		item = queue.popleft()
		if item[0] == "123450":
			return item[1]
		start = [i for i,j in enumerate(item[0]) if j=="0"][0]
		nbors = []
		for i in get_nbors(item[0],start):
			s = swap(item[0],start,i)
			nbors.append(s)
		for nbor in nbors:
			if nbor not in visited:
				visited.add(nbor)
				queue.append((nbor,item[1]+1))
	return -1




k = sol(board)
print(k)

# print(swap("123405",1,4))