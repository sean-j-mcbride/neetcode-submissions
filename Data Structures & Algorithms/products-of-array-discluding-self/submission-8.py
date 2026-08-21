class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums[0] == 0:
            zero = 1
            product = 1
        else:
            zero = 0
            product = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != 0:
                product = product * nums[i]
            else:
                zero += 1
        print(zero)
        output = []

        for num in nums:
            if num == 0 and zero == 1:
                output.append(product)
            elif num == 0 and zero > 1:
                output.append(0)
            elif zero > 0:
                output.append(0)
            else:
                output.append(product // num)
        
        return output