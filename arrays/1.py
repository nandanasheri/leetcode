
# https://leetcode.com/problems/two-sum/description/
def twoSum(self, nums: List[int], target: int) -> List[int]:
    # two pass solution
    num_map = {}
    '''for i in range(len(nums)):
        num_map[target - nums[i]] = i
    
    for i in range(len(nums)):
        if nums[i] in num_map and num_map[nums[i]] != i:
            return [i, num_map[nums[i]]]'''
    
    # one pass solution
    for i, x in enumerate(nums):
        diff = target - x
        if diff not in num_map:
            num_map[x] = i
        else:
            return[i, num_map[diff]]