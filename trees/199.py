# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = deque()
        levels = []
        q.append(root)
        if not root:
            return []
        while q:
            new_level = []
            for i in range(len(q)):
                curr = q.popleft()
                new_level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            levels.append(new_level)
        
        for level in levels:
            result.append(level[-1])
        return result