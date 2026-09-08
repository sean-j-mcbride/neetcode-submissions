class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = " " * len(s)
        countT = Counter(t)
        countS = {}
        substring = ""

        for r in range(len(s)):
            if s[r] in countT:
                if s[r] in countS.keys():
                    countS[s[r]] += 1
                else:
                    countS[s[r]] = 1
            substring += s[r]

            while len(countS) == len(countT) and all(countS[k] >= countT[k] for k in countS.keys()):
                res = substring if len(substring) <= len(res) else res
                if s[l] in countS:
                    countS[s[l]] -= 1
                    if countS[s[l]] == 0:
                        del countS[s[l]]
                l += 1
                substring = substring[1:]
        
        return res if res != " " * len(s) else ""
