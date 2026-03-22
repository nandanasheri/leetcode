'''
       l   r
"a b c i i i d e f" k = 3
set of vowels = {a,e,i,o,u}
numVowels = 3
result = 3


'''
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        numVowels = 0
        for i in range(k):
            if s[i] in vowels:
                numVowels += 1
        
        result = numVowels
        l,r = 0, k
        
        while r < len(s):
            if s[l] in vowels:
                numVowels -= 1
            l += 1
            if s[r] in vowels:
                numVowels += 1
            result = max(result, numVowels)
            r += 1

        return result
            