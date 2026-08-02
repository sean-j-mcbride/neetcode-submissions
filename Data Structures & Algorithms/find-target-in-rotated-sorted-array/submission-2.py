class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pivot = 0

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < nums[pivot]:
                    pivot = l
                break
            
            m = (l + r) // 2
            if nums[m] < nums[pivot]:
                    pivot = m

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        l, r = 0, len(nums) - 1

        if pivot != 0:
            if target <= nums[r]:
                l = pivot
            else:
                r = pivot - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
            