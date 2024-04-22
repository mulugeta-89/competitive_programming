class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r,c))
                else:
                    mat[r][c] = rows * cols

        def inbound(r, c):
            return 0 <= r < len(mat) and 0 <= c < len(mat[0])

        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        while queue:
            r, c = queue.popleft()
            for x, y in directions:
                new_r, new_c = r + x, c + y
                if inbound(new_r, new_c) and mat[new_r][new_c] > mat[r][c] + 1:
                    queue.append((new_r, new_c))
                    mat[new_r][new_c] = mat[r][c] + 1
        return mat
