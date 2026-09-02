class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            num_map[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_map and num_map[diff] != i:
                return [i, num_map[diff]]
        return []
        
        
