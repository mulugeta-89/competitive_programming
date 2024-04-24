class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        heap = []
        for index, item in enumerate(tasks):
            item.append(index)
        tasks.sort(key = lambda x: x[0])
        sol = []
        i, time = 0, 0
        while heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heappush(heap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not heap:
                time = tasks[i][0]
            else:
                procTime, idx = heappop(heap)
                time += procTime
                sol.append(idx)
        return sol

        