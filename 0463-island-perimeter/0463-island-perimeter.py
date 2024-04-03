class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        direction = [(-1,0), (0,1), (1,0), (0, -1)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(grid, visited, row, col):
            nonlocal count
            visited[row][col] = True

            for i, j in direction:
                new_row = row + i
                new_col = col + j

                if inbound(new_row, new_col) and not visited[new_row][new_col] and grid[new_row][new_col]:
                    dfs(grid, visited, new_row, new_col)
                elif not inbound(new_row, new_col) or not grid[new_row][new_col]:
                    count += 1
            return count
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return dfs(grid, visited, r , c)