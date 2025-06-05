# o(n) time AND space - we can do better with space
class Solution:
    def trap(self, height: list[int]) -> int:
        max_l = height[0]
        max_r = height[-1]
        l = 0
        r = len(height)  - 1

        result = 0

        while l < r:
            if height[l] <= height[r]:
                water = max_l - height [l]
                max_l = max(max_l, height[l])
                l += 1
            else:
                water = max_r - height [r]
                max_r = max(max_r, height[r])
                r -= 1
            
            result +=  water * (water > 0)


        # o(n) time and space solution
        '''l_arr = [0]  * len(height)
        r_arr = [0]  * len(height)
        
        l_max = 0
        for i in range(1, len(height)):
            l_max = max(l_max, height[i-1])
            l_arr[i] = l_max
        
        r_max = 0
        for i in range(len(height)-2, -1, -1):
            r_max = max(r_max, height[i+1])
            r_arr[i] = r_max
        
        result = 0
        for i in range(len(height)):
            water =  min(l_arr[i], r_arr[i]) - height[i]
            result +=  water * (water > 0)'''
        
        return result