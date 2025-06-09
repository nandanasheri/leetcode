# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i,h in enumerate(heights):
            start = i # this is the index to extend in backwards
            while len(stack) > 0 and stack[-1][1]> h:
                top_i, top_h = stack.pop()
                max_area = max(max_area, top_h * (i-top_i))
                start = top_i
            
            stack.append((start,h))

        for i,h in stack:
            max_area = max(max_area, h * (len(heights)- i))
        
        return max_area