class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, stack, opened):
            if len(path) == n * 2:
                res.append(path)
                return
            
            if opened < n:
                stack.append("(")
                backtrack(path + "(", stack, opened + 1)
                stack.pop()
            if stack:
                stack.pop()
                backtrack(path + ")", stack, opened)
                stack.append("(")

        backtrack("", [], 0)
        return res