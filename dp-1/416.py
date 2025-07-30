class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False
        find = total // 2

        sum_set = set()

        sum_set.add(0)
        sum_set.add(nums[-1])

        for i in range(n-2, -1, -1):
            sum_set_copy = set()
            for j in sum_set:
                if j + nums[i] == find:
                    return True
                sum_set_copy.add(j + nums[i])
                sum_set_copy.add(j)
            sum_set = sum_set_copy

        return False
        