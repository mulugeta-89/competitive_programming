class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]
        graph = defaultdict(list)
        graph_indegree = defaultdict(int)
        visited = set()
        for x, y in prerequisites:
            graph[y].append(x)
            graph_indegree[x] += 1

        queue = deque()
        for k in range(numCourses):
            if graph_indegree[k] == 0:
                queue.append(k)
                visited.add(k)
        sol = []
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                sol.append(node)
                for neighbour in graph[node]:
                    graph_indegree[neighbour] -= 1
                    if neighbour not in visited and graph_indegree[neighbour] == 0:
                        queue.append(neighbour)
                        visited.add(neighbour)
        return sol if len(sol) == numCourses else []
                    

        