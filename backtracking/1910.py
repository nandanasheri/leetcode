'''
a b c
d a b a a b c b c
s = 
i = 0 -> n
j -> iterating through part
.index() -> first occurence
if no occurence of part -> return s
reset s
'''
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if part not in s:
            return s
        ind = s.index(part)
        return self.removeOccurrences(s[0:ind]+s[ind+len(part):],part)