class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        a = gcd(*list(count.values()))
        return a > 1