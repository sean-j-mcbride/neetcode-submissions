class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesCopy = stones.copy()
        maxHeap = [(-1) * stone for stone in stonesCopy]

        while len(maxHeap) > 1:
            heapq.heapify(maxHeap)
            x = (-1) * heapq.heappop(maxHeap)
            heapq.heapify(maxHeap)
            y = (-1) * heapq.heappop(maxHeap)

            if x < y:
                y = y - x
                heapq.heappush(maxHeap, (-1) * y)
            elif y < x:
                x = x - y
                heapq.heappush(maxHeap, (-1) * x)
        return (-1) * maxHeap[0] if len(maxHeap) == 1 else 0