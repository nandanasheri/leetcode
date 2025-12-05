# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        paths = 0
        levelsums = [0]

        def dfs(curr, currsum):
            nonlocal paths
            # print(levelsums, paths)
            if not curr:
                return
            currsum += curr.val
            # we keep track of every level and then we check if removing a sum would reach us the right target
            for s in range(len(levelsums)):
                if currsum - levelsums[s] == targetSum:
                    paths += 1

            levelsums.append(currsum)
            dfs(curr.left, currsum)
            dfs(curr.right, currsum)
            currsum -= curr.val
            levelsums.pop()
        
        dfs(root,0)
        return paths


