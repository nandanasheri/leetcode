class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        countmap = {}
        for i in s:
            if i not in countmap:
                countmap[i] = 1
            else:
                countmap[i] += 1
        
        length = 0
        flag = False
        for i in countmap:
            if countmap[i] % 2 == 0:
                length += countmap[i]
            else:
                # add highest possible count of even letters
                length += countmap[i] - 1
                flag = True
        
        #there was at least one odd number of letters so we can place one letter in the middle of the palindrome
        if flag:
            return length+1
        else:
            return length

        