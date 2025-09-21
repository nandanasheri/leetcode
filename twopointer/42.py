class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        maxL = [0] * len(height)
        maxR = [0] * len(height)

        for i in range(1, len(height)):
            maxL[i] = (max(height[i-1], maxL[i-1]))
        
        for i in range(len(height)-2, -1, -1):
            maxR[i] = max(height[i+1], maxR[i+1])
        
        res = 0

        for i in range(len(height)):
            curr_h = min(maxL[i], maxR[i]) - height[i]
            if curr_h > 0:
                res += curr_h

        return res
