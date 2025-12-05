'''nums = [-1,2,1,-4] target = 1
a b c close to target -> minimize the difference (target - (a+b+c)) as small as possible
return a + b + c

diff = 3
brute force o(n^2)
                i   l   r
sorted nums => [-4,-1,1,2]
targetdiff = target - nums[i] = 5

for i in range(nums):
    l = i + 1
    r = len(nums) - 1
    while l < r:
        # diff is zero
        if sum == target:
            return sum
        if target - (nums[i] + nums[l] + nums[r]) < minimumdiff:
            reset minimumdiff
            keep track of sum
        # if larger
        if nums[i] + nums[l] + nums[r] < target:
            l += 1
        else:
            r -=1 
return minimumsum
        
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        minimum_diff = float("inf")
        minimum_sum = 0
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums)-1
            curr = nums[i]
            while l < r:
                tempsum = curr + nums[l] + nums[r]
                # difference is as low as it gets so quick return
                if tempsum == target:
                    return tempsum
                # effectively trying to minimize difference
                if abs(tempsum-target) < minimum_diff:
                    minimum_diff = abs(tempsum-target)
                    minimum_sum = tempsum
                # shifting pointers if sum is either too small or too big
                if tempsum > target:
                    r -= 1
                else:
                    l += 1
        
        return minimum_sum

        