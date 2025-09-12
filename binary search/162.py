class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r :
            # print(l, r)
            mid = (l+r) // 2

            left, right = 0,0

            if mid - 1 < 0:
                left = float("-infinity")
            else:
                left = nums[mid-1]
            
            if mid + 1 >= len(nums):
                right = float("-infinity")
            else:
                right = nums[mid+1]
            
            if nums[mid] > left and nums[mid] > right:
                return mid
            
            if nums[mid] < left:
                r = mid - 1
            else:
                l = mid + 1