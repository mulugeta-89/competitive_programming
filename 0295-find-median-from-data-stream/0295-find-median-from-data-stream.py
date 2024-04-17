class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []     

    def addNum(self, num: int) -> None:
        heappush(self.min_heap, num)
        if len(self.min_heap) - len(self.max_heap) > 1:
            x = heappop(self.min_heap)
            heappush(self.max_heap, -1*x) 
        while len(self.max_heap) > 0 and len(self.min_heap) > 0 and -1*self.max_heap[0] > self.min_heap[0]:
            x = heappop(self.min_heap)
            y = heappop(self.max_heap)

            heappush(self.min_heap, -1*y)
            heappush(self.max_heap, -1*x)               

    def findMedian(self) -> float:
        if len(self.min_heap) != len(self.max_heap):
            return self.min_heap[0]
        else:
            return (self.min_heap[0]+ -1*self.max_heap[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()