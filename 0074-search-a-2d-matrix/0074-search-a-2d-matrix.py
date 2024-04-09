class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        con = []
        for item in matrix:
            con.extend(item)
        l, r = 0, len(con)-1
        while l <= r:
            mid = (l+r)//2
            if con[mid] == target:
                return True
            elif target < con[mid]:
                r = mid -1
            else:
                l = mid + 1
        return False
        