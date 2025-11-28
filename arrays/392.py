class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        matches = 0
        ind_s, ind_t = 0, 0
        while ind_s < len(s) and ind_t < len(t):
            if s[ind_s] == t[ind_t]:
                matches += 1
                ind_s += 1
            ind_t += 1
        if matches == len(s):
            return True
        else:
            return False