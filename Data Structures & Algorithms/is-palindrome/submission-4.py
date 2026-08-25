class Solution:
    def isPalindrome(self, s: str) -> bool:
        front, back = 0, len(s) - 1
        while front < back:
            frontchar = s[front].lower()
            backchar = s[back].lower()
            if frontchar.isalnum() and backchar.isalnum():
                if frontchar != backchar:
                    return False
                front += 1
                back -= 1
            elif not frontchar.isalnum() and backchar.isalnum():
                front += 1
            elif frontchar.isalnum() and not backchar.isalnum():
                back -=1
            else:
                front += 1
                back -= 1
        
        return True
            
                