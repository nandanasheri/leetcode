# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) <= 1:
            return nums[0]

        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l+r) // 2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1 
        return res

        # while l <= r:
        #     mid = (l+r) // 2
        #     if nums[mid-1] > nums[mid]:
        #         return nums[mid]
        #     if nums[l] < nums[mid]:
        #         if nums[mid] >= nums[r]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     else:
        #         if nums[mid] < nums[r]:
        #             r = mid - 1
        #         else:
        #             l = mid + 1