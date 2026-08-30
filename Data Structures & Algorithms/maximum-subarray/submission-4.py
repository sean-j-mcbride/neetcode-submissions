class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maximum = max(maximum, curSum)
        return maximum
        