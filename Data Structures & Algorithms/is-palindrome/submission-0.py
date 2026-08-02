class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = "".join(char for char in s if char.isalnum()).lower()
        l = len(cleaned_string)
        for i in range(l // 2):
            if cleaned_string[i] != cleaned_string[l - 1 - i]:
                return False
        return True

        