class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        '''
        all the issues i faced was with bounds for the while loop
        you don't technically need to clean the string - just skip over any characters that are not alpha numeric
        '''
        # clean = ""

        # for i in s:
        #     if i.isalnum():
        #         clean += i.lower()
        
        # if len(clean) == 0:
        #     return True
    
        l = 0
        r = len(s)-1
        
        while l < r :
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False

        return True

            
        