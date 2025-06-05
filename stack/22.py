# https://leetcode.com/problems/generate-parentheses/
# recursive solution 2^n
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def  _generateParan(stack, num_open, num_close):
            if num_open == num_close and num_open == n:
                result.append(stack)
                return

            elif num_open == num_close:
                _generateParan(stack+"(", num_open+1, num_close)
            
            elif num_open > num_close and num_open == n:
                _generateParan(stack+")", num_open, num_close+1)

            elif num_open > num_close:
                _generateParan(stack+"(", num_open+1, num_close)
                _generateParan(stack+")", num_open, num_close+1)
    
        _generateParan("", 0, 0)
        return result

