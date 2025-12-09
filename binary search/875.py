class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1, max(piles)
        res = r
        while l <= r:
            mid =(l+r) // 2
            curr_h = 0
            for p in piles:
                curr_h += math.ceil(p/mid)
            # print(l,r,mid, curr_h)
            if curr_h <= h:
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
        