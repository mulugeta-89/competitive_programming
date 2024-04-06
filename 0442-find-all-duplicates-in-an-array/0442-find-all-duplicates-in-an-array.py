class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            correct = nums[i]-1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        sol = []
        for i in range(n):
            if nums[i]-1 != i:
                sol.append(nums[i])
        return sol
        