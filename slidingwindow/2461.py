'''
 0 1 2 3 4 5 6
[1,5,4,2,9,9,9]
           l
k = 3
i = 0
j = 0, 1, 2
brute force -> every possible subarray, compare len == k, keep track of sum max(sum)
only need to check for subarrays of length k
i = 0 [1,5,4]
i => 0 -> n-k
 subarray =[i:i+k]
 check if subarray is valid - are elements distinct?
 [2,9,9] -> set() compare if len(set) == k : update our sum
 else: continue
 elements are distinct ?

 o(n*k)
'''
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currsum = 0
        l = 0
        unique = set()
        for r in range(len(nums)):
            # window is too big or element is not distinct
            while r-l+1 > k or nums[r] in unique:
                currsum -= nums[l]
                unique.remove(nums[l])
                l += 1
            currsum += nums[r]
            unique.add(nums[r])
            # valid window
            if r-l+1 == k:
                res = max(res, currsum)   
        return res