class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        dest = (len(grid)-1, len(grid[0])-1)
        directions = { 'E': (0,1), 'W': (0,-1), 'N': (-1,0), 'S': (1,0)}
        visited = set()
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        valid_path = {
            1: {'E': [1, 3, 5], 'W': [1, 4, 6]},
            2: {'N': [2, 3, 4], 'S': [2, 5, 6]},
            3: {'W': [1, 4, 6], 'S': [2, 5, 6]},
            4: {'E': [1, 3, 5], 'S': [2, 5, 6]},
            5: {'N': [2, 3, 4], 'W': [1, 4, 6]},
            6: {'N': [2, 3, 4], 'E': [1, 3, 5]},
        }

        def dfs(i,j):
            if (i,j) == dest:
                return True
            visited.add((i, j))
            for dr, valid_direct in valid_path[grid[i][j]].items():
                new_row, new_col = i + directions[dr][0], j + directions[dr][1]

                if (new_row, new_col) not in visited and inbound(new_row, new_col):
                    if grid[new_row][new_col] in valid_direct:
                        if dfs(new_row, new_col):
                            return True
            return False
        return dfs(0,0)



