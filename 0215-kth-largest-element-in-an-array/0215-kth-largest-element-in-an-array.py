class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1*num for num in nums]
        heapify(nums)

        for i in range(k):
            x = heappop(nums)
        return -(x)
        