class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-v for v in count.values()]

        q = deque()
        time = 0

        heapq.heapify(maxHeap)
        while maxHeap or q:
            time += 1
            
            if maxHeap:
                cur = heapq.heappop(maxHeap)
                if cur + 1 != 0: q.append((cur + 1, n + time))
            
            if q:
                if time == q[0][1]:
                    heapq.heappush(maxHeap, q.popleft()[0])
        return time
