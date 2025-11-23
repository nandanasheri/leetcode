class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)-1):
                diff = target - (nums[i] + nums[j])
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] == diff:
                        res.add((nums[i],nums[j],nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > diff:
                        r -=1 
                    else:
                        l += 1
        
        res_list = []
        for each in res:
            res_list.append(list(each))
        return res_list
