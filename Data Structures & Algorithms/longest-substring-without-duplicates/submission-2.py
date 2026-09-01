class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr = 0
        temp = ""

        for i, letter in enumerate(s):
            while letter in temp:
                temp = temp[1:]
                curr -= 1
            temp += letter
            curr += 1
            longest = max(longest, curr)
        return longest
                