class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        quad = []

        def kSum(k, start, target):
            # recursive step
            if k != 2:
                for i in range(start, len(nums)-k+1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i+1, target-nums[i])
                    quad.pop()
            # base case - two pointer 2Sum
            if k == 2:
                diff = target
                l = start
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == diff:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l+= 1
                    elif nums[l] + nums[r] > diff:
                        r -=1 
                    else:
                        l += 1
        
        kSum(4, 0, target)
        return res
