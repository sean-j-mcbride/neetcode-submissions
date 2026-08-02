class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        maximum = 0
        total = 0

        for h in height:
            maximum = max(h, maximum)
            prefix.append(maximum)

        maximum = 0

        for h in height[::-1]:
            maximum = max(h, maximum)
            suffix.insert(0, maximum)
        
        for i in range(len(height) - 1):
            current = min(prefix[i], suffix[i]) - height[i]
            total += current
        return total
