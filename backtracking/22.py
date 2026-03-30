'''
n = 2
curr = 
result = ()(), (())
open = 0
closed = 0
open_p = 0, closed_p = 0
curr = [(]
if open == close == n:
    append to result using .join()
    return
if open == close:
    append (
    func(open + 1, closed)
    pop()
elif open > close:
    append )
    func()
    pop()
    OR 
    append ( only if open < n
    func()
    pop()
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        curr = []
        
        def _generate(openp, closed):
            if openp == closed and openp == n:
                result.append("".join(curr))
                return
            # add an open because equal num 
            if openp == closed:
                curr.append("(")
                _generate(openp+1, closed)
                curr.pop()
            # more opnened than closed
            elif openp > closed:
                # close an opened parantheses
                curr.append(")")
                _generate(openp, closed+1)
                curr.pop()
                # not enough open? open more
                if openp != n:
                    curr.append("(")
                    _generate(openp+1, closed)
                    curr.pop()
        
        _generate(0,0)
        return result
        