class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = len(nums) - 1
        # find position that it stops increasing from backwards
        while pivot > 0:
            if nums[pivot] <= nums[pivot-1]:
                pivot -= 1
            else:
                break
        # complete descending order - sort and return
        if pivot == 0:
            nums.sort()
            return nums
        
        # until pivot, make it ascending instead
        l,r = pivot, len(nums)-1
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        target = nums[pivot - 1]
        large = 1000
        large_ind = 0
        # find next number to swap the pivot pos with
        for i in range(pivot, len(nums)):
            if nums[i] > target and nums[i] < large:
                large = nums[i]
                large_ind = i
        
        nums[large_ind], nums[pivot-1] = nums[pivot-1], nums[large_ind]
            
        