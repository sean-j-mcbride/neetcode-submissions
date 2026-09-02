class Solution:
    def isValid(self, s: str) -> bool:
        opened, closed = ['(', '{', '['], [')', '}', ']']
        stack = []

        if len(s) % 2 != 0:
            return False

        for c in s:
            if c in opened:
                stack.append(c)
            elif c in closed:
                if not stack:
                    return False
                elif c == ')'and stack[-1] != '(':
                    return False
                elif c == '}' and stack[-1] != '{':
                    return False
                elif c == ']' and stack[-1] != '[':
                    return False
                stack.pop()
        return True if not stack else False