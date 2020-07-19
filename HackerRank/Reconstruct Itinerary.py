from collections import defaultdict,deque

def build_graph(tickets):
    graph = defaultdict(list)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
    # graph[ticket[1]].append(ticket[0])
    for i in graph:
        graph[i] = sorted(graph[i])
    return graph

def dfs(graph, start):
    visited = set()
    visited.add(start)
    stack = deque([start])
    while stack:
        item = stack.pop()
        yield item
        nbors = graph[item]
        for nbor in nbors:
            if nbor not in visited:
                visited.add(nbor)
                stack.append((nbor))
    
def sol(tickets):
    g = build_graph(tickets)
    print(g)
    return list(dfs(g,"JFK"))

t1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
t2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

# print(sol(t1))

print(sol(t2))

targets = defaultdict(list)
for a, b in sorted(t2)[::-1]:
    targets[a] += b

print(targets)