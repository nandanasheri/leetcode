class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        for i in range(0, len(s)//2):
            substr = s[0:i+1]
            sub_len = len(substr)
            
            matches = 0
            for j in range(0, len(s), sub_len):
                if s[j:j+sub_len] != substr:
                    break
                else:
                    matches += 1
            if matches == len(s) / sub_len:
                return True
        return False