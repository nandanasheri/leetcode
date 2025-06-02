def containsDuplicate(self, nums: List[int]) -> bool:
        # first appraoch, sort and check adjacent elements - O(nlogn) time, we can do better!
        '''sorted(nums)
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False'''

        # second approach, hash map O(n) time AND space
        hashmap = {}
        for i in range(0, len(nums)):
            if nums[i] in hashmap:
                return True 
            else:
                hashmap[nums[i]] = i
        return False