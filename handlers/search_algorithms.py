# Function for finding a path using DFS
def dfs(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        return path
    if not graph.has_node(start) or not graph.has_node(end):
        return None
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs(graph, neighbor, end, path + [neighbor])
            if new_path is not None:
                return new_path
    return None


# Function for finding a path using Breadth-First Search
def bfs(graph, start, end):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == end:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None
