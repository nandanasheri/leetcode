# https://leetcode.com/problems/container-with-most-water/
# o(n) time o(1) space

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            curr_height = min(height[l], height[r])
            area = (r-l) * curr_height
            if curr_height == height[l]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, area)
        
        return max_area