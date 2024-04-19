class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dicti = Counter(words)
        dicti = (sorted(dicti.items(), key=lambda x: (-x[1], x[0])))
        return [k for k,y in dicti[:k]]


        