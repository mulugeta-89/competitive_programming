class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        time, fresh = 0, 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append([i,j])
        print(queue)
        directions = [[-1,0], [0,1], [1,0], [0,-1]]
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for x, y in directions:
                    new_r, new_c = r + x, c + y

                    if inbound(new_r, new_c) and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append([new_r, new_c])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1


        