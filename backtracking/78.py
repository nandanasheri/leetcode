class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []

        def generate_subsets(i):
            if i == len(nums):
                result.append(curr[::])
                # print(curr)

                return
            generate_subsets(i+1)
            curr.append(nums[i])
            generate_subsets(i+1)
            curr.pop()

        
        generate_subsets(0)
        return result