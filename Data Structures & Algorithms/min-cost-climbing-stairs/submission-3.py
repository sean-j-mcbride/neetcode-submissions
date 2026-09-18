class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = cur = 0
        for c in cost:
            prev, cur = cur, min(prev, cur) + c
        return min(prev, cur)