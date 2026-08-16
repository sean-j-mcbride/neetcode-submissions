class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return "@@@"
        return ",@".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "@@@": return []
        checkp = 0
        idx = 0
        out = []
        while idx < len(s):
            if s[idx:idx+2] == ",@":
                out.append(s[checkp:idx])
                checkp, idx = idx + 2, idx + 2
            else:
                idx += 1
        out.append(s[checkp:])
        return out
