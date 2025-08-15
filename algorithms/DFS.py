def dfs_graph (graph, node, visited):
    if node in visited:
        return
    visited.add(node)
    print(node)
    for neighbor in graph[node]:
        dfs_graph (graph, neighbor, visited)

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

visited = set()
dfs_graph(graph, 'A', visited)