class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, n in enumerate(nums):
            numMap[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in numMap and numMap[diff] != i:
                return [i, numMap[diff]]
