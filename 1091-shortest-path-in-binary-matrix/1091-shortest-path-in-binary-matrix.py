class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def inbound(r,c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        directions = [[-1,0], [0,1],[1,0],[0,-1],[-1,1],[1,1],[1,-1],[-1,-1]]
        queue = deque()
        queue.append([0,0,1])
        visited = set()
        visited.add((0,0))
        count =  0
        if grid[0][0] != 0:
            return -1
        while queue:
            r, c, dst = queue.popleft()
            if r == len(grid)-1 and c == len(grid[0])-1:
                return dst
            for x , y in directions:
                new_r, new_c = r + x, c + y

                if (new_r, new_c) not in visited and inbound(new_r, new_c) and grid[new_r][new_c] == 0:
                    queue.append([new_r, new_c, dst+1])
                    visited.add((new_r, new_c)) 
        return -1

