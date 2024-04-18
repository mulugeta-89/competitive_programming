class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = Counter(nums)
        dicti = sorted(dicti.items(), key=lambda x: x[1], reverse=True)
        sol = dicti[:k]
        return [x for x, y in sol]

        