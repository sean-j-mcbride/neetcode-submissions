class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(path, index):
            if index == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[index])
            backtrack(path, index + 1)
            path.pop()
            j = index + 1
            while j < len(nums) and nums[j] == nums[index]:
                j += 1
            backtrack(path, j)
        
        backtrack([], 0)
        return res