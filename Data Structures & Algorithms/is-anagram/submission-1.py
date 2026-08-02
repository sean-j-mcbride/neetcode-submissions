class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        for letter in s:
            if letter not in hashS.keys():
                hashS[letter] = 1
            else:
                hashS[letter] += 1

        for letter in t:
            if letter not in hashT.keys():
                hashT[letter] = 1
            else:
                hashT[letter] += 1
        
        return hashS == hashT