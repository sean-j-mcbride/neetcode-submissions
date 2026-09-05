class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            h = -heapq.heappop(maxHeap)
            secondH = -heapq.heappop(maxHeap)
            new = h - secondH
            if new != 0:
                heapq.heappush(maxHeap, -new)
        
        if maxHeap:
            return -maxHeap[0]
        return 0