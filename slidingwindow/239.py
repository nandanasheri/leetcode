class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque([])
        result = []
        l = 0

        for r in range(len(nums)):
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)  
            # if we go to new window we want to remove any old elements
            if l > deq[0]:
                deq.popleft()      
            if r + 1 >= k:
                result.append(nums[deq[0]])
                l += 1
        
        return result
            
