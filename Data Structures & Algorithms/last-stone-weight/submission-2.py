class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:    
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)

            if x < y:
                y = y - x
                heapq.heappush(maxHeap, -y)
            elif y < x:
                x = x - y
                heapq.heappush(maxHeap, -x)
        return abs(maxHeap[0]) if len(maxHeap) == 1 else 0