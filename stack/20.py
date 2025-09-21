class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_p = set(["(", "[", "{"])

        for i in s:
            if i in open_p:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if (i == ")" and top == "(") or (i == "]" and top == "[") or (i == "}" and top == "{"):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
        