class Solution:
    def validPalindrome(self, s: str) -> bool:
        # check for a mismatch, if we find a mismatch, then check for both cases by removing each char
       
        l = 0
        r = len(s) - 1
        mismatch = 0

        while l < r:

            if s[l] != s[r]:
                # we already had a mismatch
                if mismatch > 1:
                    return False
                # case 1 - remove s[l] from s
                substr_s = s[l+1:r+1]
                reverse_s = substr_s[::-1]
                if substr_s == reverse_s:
                    mismatch = 1
                    l += 1
                    continue
                # case 2 - remove s[r] from s
                substr_s = s[l:r]
                reverse_s = substr_s[::-1]
                if substr_s == reverse_s:
                    mismatch = 1
                    r -= 1
                    continue
                # neither cases of removing a character resulted in a palindrome, return False
                else:
                    return False
            l += 1
            r -=1
        
        return True
            