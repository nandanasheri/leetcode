class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        d = collections.deque()

        l, r = 0,0

        while r < len(nums):
            # if smaller values exist, pop from the queue's front
            while len(d) > 0 and nums[d[-1]] < nums[r]:
                d.pop()
            # push to the back of the queue
            d.append(r)

            # check if we are out of bounds - remove the front value if true
            if l > d[0]:
                d.popleft()
            # we are at size k - this edge case is only for the first time then we always move l and r together!!
            if (r + 1) >= k:
                output.append(nums[d[0]])
                l += 1
            r += 1
        
        return output

