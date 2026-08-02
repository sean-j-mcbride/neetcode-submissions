class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setOfInts = set(nums)
        if len(setOfInts) == len(nums):
            return False
        return True