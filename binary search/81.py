'''
 0 1 2 3 4 
[1,0,1,1,1] target = 0

0, 4 mid = 2
l = 0 r = 3 mid = 1
# mid is in right sorted half
if mid == target: return true
if mid < r
    if mid < target < r:
        l = mid + 1
    else:
        r = mid - 1
# if mid is in left sorted half
else:
    if l < target < mid:
        r = mid - 1
    else:
        l = mid + 1

'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            # print(l,r,mid)
            if nums[mid] == target:
                return True
            if nums[mid] == nums[r]:
                r -= 1
                continue
            if nums[mid] < nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False