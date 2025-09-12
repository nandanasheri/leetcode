class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open, max_open = 0,0

        
        for i in s:
            if i == "(":
                min_open += 1
                max_open += 1
            if i == ")":
                min_open -= 1
                max_open -= 1
            if i == "*":
                max_open += 1
                min_open -= 1
            if min_open < 0:
                min_open = 0
            if max_open < 0:
                return False

        return max_open == 0 or min_open == 0

