from Graph import Graph
from collections import defaultdict, deque


def add_edge(graph, vertex_a, vertex_b):
	graph[vertex_a].add(vertex_b)
	graph[vertex_b].add(vertex_a)


def build_graph(board_size):
	graph = defaultdict(set)
	for row in range(board_size):
		for col in range(board_size):
			for to_row, to_col in legal_moves_from(row, col, board_size):
				add_edge(graph, (row, col), (to_row, to_col))

	vertices = [x for x in graph]
	edges = []

	for i in graph:
		for j in graph[i]:
			edges.append([i,j])

	graph = Graph()


	for i in vertices:
		graph.add_vertex(i)

	for i in edges:
		graph.add_edge(*i)

	return graph, vertices, edges

MOVE_OFFSETS = (
			  (-1, -2), ( 1, -2),
	(-2, -1),                     ( 2, -1),
	(-2,  1),                     ( 2,  1),
			  (-1,  2), ( 1,  2),
)


def legal_moves_from(row, col, board_size):
	for row_offset, col_offset in MOVE_OFFSETS:
		move_row, move_col = row + row_offset, col + col_offset
		if 0 <= move_row < board_size and 0 <= move_col < board_size:
			yield move_row, move_col

def dfs_rec(graph, start, visited = []): #it can be bfs
	if start not in visited:
		visited.append(start)
		for neighbor in graph.get_neighbors(start):
			dfs_rec(graph, neighbor, visited)	
	return visited	




if __name__ == "__main__":


	dimension = 8
	graph, vertices, edges = build_graph(dimension)
	count = 0
	for v in vertices:

		visited = dfs_rec(graph,v)
		if len(set(visited)) == dimension*dimension:
			
			count+=1
			# print(v)
			# print(visited)
			# print("\n\n")
	print(count)

	

