class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # global res
        # res = 0
        # stairs = []

        # def _climbstairs(stairs):
        #     global res
        #     if sum(stairs) == n:
        #         res += 1
        #         return
        #     if sum(stairs) > n:
        #         return
        #     stairs.append(1)
        #     _climbstairs(stairs)
        #     stairs.pop()
        #     stairs.append(2)
        #     _climbstairs(stairs)
        #     stairs.pop()

        # _climbstairs(stairs)
        # return res

        one = 1
        two = 1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
            

        