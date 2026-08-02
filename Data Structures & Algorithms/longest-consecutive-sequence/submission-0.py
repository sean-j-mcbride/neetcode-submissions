class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = len(nums)
        set_nums = set(nums)
        start = []
        highest = 0

        for i in range(length):
            if (nums[i] - 1) not in nums:
                start.append(nums[i])
        
        for s in start:
            tracker = s
            counter = 1

            while (tracker + 1) in set_nums:
                counter += 1
                tracker += 1
            
            if counter > highest:
                highest = counter

        return highest


            