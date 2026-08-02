class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        out = []
        nums.sort() 

        for i in range(l - 2):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]

            j, k = i + 1, l - 1

            while j < k:
                current_sum = nums[j] + nums[k]

                if current_sum < target:
                    j += 1
                elif current_sum > target:
                    k -= 1
                else:
                    out.append([nums[i], nums[j], nums[k]])
                    
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                    
        return out


                    

            
