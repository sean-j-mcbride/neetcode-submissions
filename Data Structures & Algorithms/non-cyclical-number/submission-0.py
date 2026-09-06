class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while n != 1 and n not in seen:
            seen.append(n)
            temp = str(n)
            n = sum(int(digit)**2 for digit in temp)
            
        return True if n == 1 else False
        