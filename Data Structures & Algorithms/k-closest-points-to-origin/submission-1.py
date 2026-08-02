class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [(-(p[0]**2 + p[1]**2), [p[0], p[1]]) for p in points]
        res = []
        heapq.heapify(minHeap)
        for i in range(len(minHeap) - k):
            heapq.heappop(minHeap)
        
        res = [value[1] for value in minHeap]
        return res
