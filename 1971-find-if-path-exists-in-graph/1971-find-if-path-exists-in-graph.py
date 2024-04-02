def construct_graph(edges):
    graph = defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    return graph
def dfs(graph, source, destination, visited):
    if source == destination:
        return True
    visited.add(source)
    for item in graph[source]:
        if item not in visited:
            found = dfs(graph, item, destination, visited)
            if found:
                return True
    return False
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = construct_graph(edges)
        visited = set()
        return dfs(graph, source, destination,visited)
        