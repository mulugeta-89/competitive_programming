"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        count = 0
        visited = set()
        def buildGraph(employees):
            building = defaultdict(list)
            for emp in employees:
                for item in emp.subordinates:
                    building[emp.id].append(item)
                building[emp.id].append(emp.importance)
            return building
        graph = buildGraph(employees)
        def dfs(graph, id, visited):
            nonlocal count
            if id in visited:
                return False
            visited.add(id)
            print(graph[id])
            if len(graph[id]) > 0:
                count += graph[id][-1]
            for neighbour in range(len(graph[id])-1):
                dfs(graph, graph[id][neighbour], visited)
            return count
        return dfs(graph, id, visited)
