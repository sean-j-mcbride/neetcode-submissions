class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, num in enumerate(nums):
            indices[num] = i
        
        for i, num in enumerate(nums):
            comp = target - num
            if comp in indices and indices[comp] != i:
                return [i, indices[comp]]
        return []
