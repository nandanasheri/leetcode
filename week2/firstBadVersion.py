# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        ''' looked through a discussion for an approach but binary search works by 
        only calling API at mid and depending on the return value moving hi and lo values
        accordingly - API is only being called log(n) times'''

        lo = 1
        hi = n

        while lo <= hi :
            mid = lo + (hi - lo) // 2
            if isBadVersion(mid):
                if mid == 1:
                    return 1
                else:
                    if not isBadVersion(mid-1):
                        return mid
                    else: 
                        hi = mid - 1
            else : 
                lo = mid + 1
        