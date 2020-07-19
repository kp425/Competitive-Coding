graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]

from collections import deque

g = {}
for i,j in enumerate(graph):
    g[i] = j

print(g)


def bfs(graph):
    visited_m = set()
    visited_c = set()
    queue_m = deque([1])
    queue_c = deque([2])
    



