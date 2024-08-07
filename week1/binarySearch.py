class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        '''
        standard binary search - not much for me to change or add here
        '''
        lo = 0
        hi = len(nums) - 1
        

        while (lo <= hi):
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
        return -1
        