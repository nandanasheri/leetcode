class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        basic two map solution : o(n) solution
        i forgot you can just compare maps in python so just use equality operator space complexity is o(n+m) since we create two separate maps
        '''
        mapS = {}
        mapT = {}

        for i in s:
            if i not in mapS:
                mapS[i] = 1
            else:
                mapS[i] += 1
        
        for i in t:
            if i not in mapT:
                mapT[i] = 1
            else:
                mapT[i] += 1

        return mapS == mapT

        