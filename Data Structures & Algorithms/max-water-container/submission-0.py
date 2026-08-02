class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maximum = 0

        while left < right:
            curr = (right - left) * min(heights[left], heights[right])
            if curr > maximum:
                maximum = curr
            
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return maximum