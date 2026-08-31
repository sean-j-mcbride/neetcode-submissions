class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for c in tokens:
            if c not in operators:
                stack.append(c)
            else:
                second = int(stack.pop())
                first = int(stack.pop())
                if c == operators[0]:
                    stack.append(first + second)
                elif c == operators[1]:
                    stack.append(first - second)
                elif c == operators[2]:
                    stack.append(first * second)
                else:
                    stack.append(first / second)
        return int(stack[0])