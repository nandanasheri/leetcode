# https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = max(piles) # this is the worst possible k

        while l <= r:
            mid = (l+r) // 2
            time = 0
            for i in piles:
                time += math.ceil(i/mid)
            if time <= h:
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1
        return k
            