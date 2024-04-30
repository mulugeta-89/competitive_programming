class Solution:
    def countBits(self, n: int) -> List[int]:
        sol = []
        for i in range(n+1):
            count = 0
            while i > 0:
                if i & 1 == 1:
                    count += 1
                i >>= 1
            sol.append(count)
        return sol