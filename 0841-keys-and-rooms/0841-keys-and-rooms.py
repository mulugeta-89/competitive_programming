class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for ind, item in enumerate(rooms):
            for k in item:
                graph[ind].append(k)
        queue = deque([0])
        visited = set()
        visited.add(0)
        arr = [0]
        while queue:
            r = queue.popleft()
            for neighbour in graph[r]:
                if neighbour not in visited:
                    arr.append(neighbour)
                    queue.append(neighbour)
                    visited.add(neighbour)
        for i in range(len(rooms)):
            if i not in arr:
                return False
        return True


        