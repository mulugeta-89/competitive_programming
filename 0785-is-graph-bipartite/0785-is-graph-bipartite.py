class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1 for i in range(n)]
        def buildGraph(graph):
            built_graph = defaultdict(list)
            for ind, val in enumerate(graph):
                for item in val:
                    built_graph[ind].append(item)
            return built_graph
        def dfs(graph, node):
            ans = True
            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[node]
                    ans = ans and dfs(graph, neighbour)
                else:
                    ans = ans and  color[node] != color[neighbour]
            return ans
        graph = buildGraph(graph)
        ans = True
        for node in range(n):
            if color[node] == -1:
                color[node] = 0
                ans = ans and  dfs(graph, node)
        return ans
        
        
