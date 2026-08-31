class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
            
        l, r = 0, len(height) - 1
        total = 0
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                total += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                total += rightMax - height[r]
        
        return total
