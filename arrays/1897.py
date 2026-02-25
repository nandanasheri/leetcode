'''
"aabc","bc"
a -> (0,0) (0,3)
b -> (0,1) (1,0)
c -> (0,2) (1,1)

check if all strings are equal
["abc","aabc","bc"]
a = 3
b = 3
c = 3
n = 3 number of words
freq % n == 0 -> if true for every character, then return true
'''
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freqs = [0] * 26
        n = len(words)
        for i in words:
            for char in i:
                freqs[ord(char) - ord('a')] += 1
        
        for f in freqs:
            if f == 0:
                continue
            if f % n != 0:
                return False
        return True
        