'''
nums = [4,1,2,2,5] k = 5
[4,1] [1,2,2]
iterate through nums
queue = []
curr = 0
result = 3
if currsum == k:
    total += 1
    pop from the queue
if curr < 5:
    i += 1
cannot guarantee sorted -> maintain order

[-1, -1, 1]
[-1, -2, -1]
[-1, 0, 1]

'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefixmap = defaultdict(int)
        # edge case for an empty prefix
        prefixmap[0] = 1
        currsum = 0
        for i in nums:
            currsum += i
            if prefixmap[currsum-k] != 0:
                result += prefixmap[currsum-k]
            prefixmap[currsum] += 1
        return result
