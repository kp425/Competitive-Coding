offsets = {"top" : (-1,0),
	"top_left" : (-1,-1),
	"top_right" : (-1,1),
	"bottom" : (1,0),
	"bottom_left" : (1,-1),
	"bottom_right" : (1,1),
	"left" : (0,-1),
	"right" : (0,1)}

l = \
[   
	[1,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[1,0,0,0]
]

m = []


def count_cells_2(l,index=(0,0), visited=set()):

	v = l[index[0]][index[1]]
	if v == 1:
		if index not in visited:
			visited.add(index)
		else:
			return 
	else:
		return 0
	
	for i in offsets.values():
		new_index = (index[0]+i[0],index[1]+i[1])
		if new_index[0]>=0 and new_index[1]>=0:
			try:
				new_value = l[new_index[0]][new_index[1]]
				if new_value == 1:
					count_cells_2(l,new_index,visited)
			except:
				pass
	return len(visited)



			


if __name__ == "__main__":

	for i in range(len(l)):
		for j in range(len(l[i])):
			k = count_cells_2(l,(i,j),set())
			print("({},{}) : {}".format(i,j,k))