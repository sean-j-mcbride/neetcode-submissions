class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in nums:
                temp = num
                count = 1
                while temp + 1 in nums:
                    count += 1
                    temp += 1
                res = max(res, count)
        return res
                    
        
