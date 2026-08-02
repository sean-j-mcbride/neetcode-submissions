class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        max_area = 0

        for i, h in enumerate(heights):
            idx_to_add = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                idx_to_add = index
            stack.append((idx_to_add, h))
            
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area



        