
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# o(n) time and space
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operands = set(['+', '-', '*', '/'])
        for i in tokens:
            if i not in operands:
                stack.append(i)
            else:
                first = int(stack.pop())
                second = int(stack.pop())
                if i == "+":
                    stack.append(first+second)
                elif i == "-":
                    stack.append(second-first)
                elif i == "*":
                    stack.append(first*second)
                elif i == "/":
                    stack.append(int(second/first))

        return int(stack[0])

