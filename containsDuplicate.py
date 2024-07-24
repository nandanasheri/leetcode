def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsSet = set()

        for each in nums:
            if each in numsSet:
                return True
            numsSet.add(each)
            
        return False

print(containsDuplicate([1,32,3,32]))