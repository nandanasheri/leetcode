# o(n) time and space
# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if len(stack) == 0: return False
                last_ele = stack[-1]
                if last_ele == "(" and i == ")":
                    stack.pop()
                elif last_ele == "[" and i == "]":
                    stack.pop()
                elif last_ele == "{" and i == "}":
                    stack.pop()
                else:
                    return False
        
        return (len(stack) == 0)