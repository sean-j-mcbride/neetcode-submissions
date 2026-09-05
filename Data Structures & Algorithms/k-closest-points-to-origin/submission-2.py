class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nlargest(k, points, key = lambda x: -math.sqrt((x[0] - 0)**2 + (x[1] - 0)**2))