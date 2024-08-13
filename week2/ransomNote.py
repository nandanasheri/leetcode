class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        '''
        this is when I really question my own abilities - simple map to keep track of characters
        just stupid sometimes tbh
        '''
        charMap = {}

        start = 'a'
        for i in range(26):
            charMap[start] = 0
            start = chr(ord(start) + 1)
        
        for i in magazine:
            charMap[i] += 1
        
        for i in ransomNote:
            if charMap[i] == 0:
                return False
            charMap[i] -= 1
        
        return True
        