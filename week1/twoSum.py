class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        '''
        Brute force - O(n^2)
        Hash Map approach - key value pairs where differnce is mapped to index position
        if the element already exists in map, then that's a two sum valid solution
        this is O(n) because dictionaries in python use hash map as the underlying implementation.
        search in hashmap is O(1) thus checking key in dictionary is constant - important to note
        '''
        
        twosumMap = {}

        for i in range(len(nums)):
            if nums[i] in twosumMap:
                return [twosumMap[nums[i]], i]
            else:
                twosumMap[target - nums[i]] = i
        
