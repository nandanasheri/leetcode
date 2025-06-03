class Solution:
    # o(n) time
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for i in nums:            
            if i-1 not in num_set:
                curr_len = 0
                while (i+curr_len) in num_set:
                    curr_len += 1
                max_len = max(curr_len, max_len)
        
        return max_len
