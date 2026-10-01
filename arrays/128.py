class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        maxlen = 0
        for num in numset:
            currlen = 1
            if num + 1 not in numset:
                while num-1 in numset:
                    currlen += 1
                    num -= 1
            maxlen = max(maxlen, currlen)
        return maxlen