class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        res = max_k

        while min_k <= max_k:
            mid = (max_k + min_k) // 2
            i = 0
            hours = 0
            while i < len(piles):
                    hours += math.ceil(float(piles[i] / mid))
                    i += 1
            if hours <= h:
                res = mid
                max_k = mid - 1
            else:
                min_k = mid + 1
        return res