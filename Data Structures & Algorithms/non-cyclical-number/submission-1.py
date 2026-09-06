class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, sum(int(digit)**2 for digit in str(n))
        while slow != fast:
            fast = sum(int(digit)**2 for digit in str(fast))
            fast = sum(int(digit)**2 for digit in str(fast))
            slow = sum(int(digit)**2 for digit in str(slow))        
        return True if fast == 1 else False