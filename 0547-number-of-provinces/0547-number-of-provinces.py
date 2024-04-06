class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def buildGraph(grid):
            n = len(grid)
            graph = defaultdict(list)
            for r in range(n):
                for c in range(n):
                    if r != c and grid[r][c] == 1:
                        graph[r].append(c)
                    else:
                        graph[r]
            return graph
        def dfs(graph, start, visited):
            if start in visited:
                return False
            visited.add(start)
            for neighbour in graph[start]:
                dfs(graph, neighbour, visited)
            return True
        graph = buildGraph(isConnected)
        visited = set()
        count = 0
        for k in graph:
            if dfs(graph, k, visited):
                count += 1
        return count
        