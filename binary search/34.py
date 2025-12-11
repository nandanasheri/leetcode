'''
start - first possible instance of target
end -> last possible instance of target
        0 1 2 3 4  5
nums = [5,7,8,8,8,10]
        l          r
start = 0, end = n-1
while l <= r:
    m = l+r // 2
    if m == target:
        # check for boundaries
    
return [-1,-1]
'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        while l <=r :
            print(l,r)
            mid = (l+r) // 2
            if nums[mid] == target:
                # check for boundaries and return
                if nums[l] == target and nums[r] == target:
                    return [l,r]
                if nums[l] != target:
                    l += 1
                if nums[r] != target:
                    r -= 1

            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return [-1,-1]