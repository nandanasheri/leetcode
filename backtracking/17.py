class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {2 : ['a', 'b', 'c'],
        3 : ['d', 'e', 'f'],
        4 : ['g', 'h', 'i'],
        5 : ['j', 'k', 'l'],
        6 : ['m', 'n', 'o'],
        7 : ['p', 'q', 'r', 's'],
        8 : ['t', 'u', 'v'],
        9 : ['w', 'x', 'y', 'z']
        }

        curr = []
        result = []

        def backtrack(i):
            if len(curr) == len(digits):
                result.append("".join(curr))
                return
            for c in mapping[int(digits[i])]:
                curr.append(c)
                backtrack(i+1)
                curr.pop()
        
        backtrack(0)
        return result