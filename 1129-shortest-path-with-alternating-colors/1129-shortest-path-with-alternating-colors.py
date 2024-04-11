class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for a, b in redEdges:
            red[a].append(b)
        for a,b in blueEdges:
            blue[a].append(b)
        
        queue = deque()
        queue.append([0,0, None]) # node, length, color
        visited = set((0, None))
        answer = [-1 for _ in range(n)]

        while queue:
            node, length, color = queue.popleft()
            if answer[node] == -1:
                answer[node] = length
            if color != "RED":
                for neighbour in red[node]:
                    if (neighbour, "RED") not in visited:
                        queue.append([neighbour, length+1, "RED"])
                        visited.add((neighbour, "RED"))
            if color != "BLUE":
                for neighbour in blue[node]:
                    if (neighbour, "bLUE") not in visited:
                        queue.append([neighbour, length+1, "BLUE"])
                        visited.add((neighbour, "BLUE"))
        return answer


