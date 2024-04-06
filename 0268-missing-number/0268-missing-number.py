class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            correct = nums[i]-1
            if nums[i] > 0:
                if nums[i] != nums[correct]:
                    nums[i], nums[correct] = nums[correct], nums[i]
                else:
                    i += 1
            else:
                i += 1
        for i in range(n):
            if nums[i]-1 != i:
                return i + 1
        return nums[0]-1
        