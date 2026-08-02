class Solution:
    def hasDuplicate(self, nums):
        unique = set(nums)
        if len(nums) == len(unique):
            return False
        return True