class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        visited = [[False for i in range(col)] for j in range(row)]
        count = 0
        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col 
        
        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        def dfs(grid, r, c, visited):
            visited[r][c] = True
            for x, y in directions:
                new_r, new_c = r + x, c + y
                if inbound(new_r, new_c) and not visited[new_r][new_c] and grid[new_r][new_c] == "1":
                    dfs(grid, new_r, new_c, visited)
            return True
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and not visited[r][c]:
                    if dfs(grid, r, c, visited):
                        count += 1
        return count




        