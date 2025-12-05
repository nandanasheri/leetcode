'''
[4,2,4,5,6]
do not need to actually remove elements
- unique elements
- subarray of unique elements -> sum of those elements 
o(n^2) every possible subarray
 0 1 2 3 4
[4,2,4,5,6]
   l
     r
  set => {2,4,5,6}
  maxscore = 17

[10000,1,10000,1,1,1,1,1,1]
  l
  
'''
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        elems = set()
        curr_score = 0
        max_score = 0
        for r in range(len(nums)):

            # while our window is invalid, slide it over
            while nums[r] in elems:
                elems.remove(nums[l])
                curr_score -= nums[l]
                l += 1
            # our window is now valid
            curr_score += nums[r]
            elems.add(nums[r])

            max_score = max(max_score, curr_score)
        
        return max_score