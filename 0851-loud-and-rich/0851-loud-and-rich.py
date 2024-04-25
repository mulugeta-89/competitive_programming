class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        graph_indegree = defaultdict(int)
        sol = [i for i in range(len(quiet))]
        for a , b in richer:
            graph[a].append(b)
            graph_indegree[b] += 1
        
        queue = deque()
        for i in range(len(quiet)):
            if graph_indegree[i] == 0:
                queue.append(i)
        quitest = quiet.copy()
        
        def bfs():
            while queue:
                rich = queue.popleft()
                for neighbour in graph[rich]:
                    if quitest[rich] < quitest[neighbour]:
                        quitest[neighbour] = quitest[rich]
                        sol[neighbour] = sol[rich]

                    graph_indegree[neighbour] -= 1
                    if graph_indegree[neighbour] == 0:
                        queue.append(neighbour)
        bfs()
        return sol

            


        