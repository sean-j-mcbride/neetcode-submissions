class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, index):
            if index == len(nums):
                new_p = sorted(path[:])
                if new_p not in res: res.append(new_p)
                return
            
            path.append(nums[index])
            backtrack(path, index + 1)
            path.pop()
            backtrack(path, index + 1)
        
        backtrack([], 0)
        return res