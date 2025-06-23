# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = None

        indices = {}

        for i in range(len(inorder)):
            indices[inorder[i]] = i

        def _buildTree(preList, inorderList):
            if not preList or not inorderList:
                return None

            root = TreeNode(preList[0])
            curr_ind = inorderList.index(root.val)
            
            # partitioning pre order list
            root.left = _buildTree(preList[1:curr_ind+1], inorderList[:curr_ind])
            root.right = _buildTree(preList[curr_ind+1:], inorderList[curr_ind+1:])
            return root

        
        return _buildTree(preorder, inorder)
        
                
            

